from manim import *
from manim_data_structures import *
class DistributionCountingSort(Scene):
    def construct(self):
        title = Tex(r"\textbf{Distribution Counting Sort}", font_size=49)
        title = title.center()
        author = Tex(r"\texttt{Ashraf Hany For The Course CS312}", font_size=29, color=YELLOW_E)
        author.next_to(title, DOWN)
        self.play(FadeIn(title), FadeIn(author))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(author))
        title = Tex(r"\textbf{In our journey through sorting algorithms, let's explore the mechanics of Distribtution Counting Sort, a non-comparison sorting technique, and its advantages to the sorting problem in using the input-enhancement technique.}",
                     font_size=31)
        title = title.center()
        self.play(FadeIn(title))
        self.wait(3)
        self.play(FadeOut(title))
        description = Text("Consider Sorting The Array", font_size=30)
        description = description.center()
        self.play(FadeIn(description))
        self.wait(1)
        self.play(description.animate.shift(1* UP+LEFT))


        # Create array from levitin
        arr = MArray(
            self,
            [13, 11, 12, 13, 12, 12],
            mob_square_args={'fill_color':  DARK_BROWN,'color': WHITE},
            mob_value_args={'color': WHITE,'font_size':28},
            mob_index_args={'color': WHITE},
            mob_arr_label_args={'color': WHITE},
            label='A',
            hide_index=True
        )       
        arr= arr.center()
        #array_rect = self.create_array(array_values)
        self.play(Write(arr))
        self.wait(1)

        # Display additional array information
        array_info = Tex(r"whose values are known to come from the set \{11, 12, 13\} and should not be \\ overwritten in the process of sorting", font_size=33)
        array_info.next_to(arr, DOWN * 1)
        self.play(Write(array_info))
        self.wait(2)
        # Fade out everything
        self.play(FadeOut(description), FadeOut(array_info),FadeOut(arr))
        arr.__hide_index = False
        array_info = Tex(r"The first step in the algorithm is to calculate the \textit{frequency} and the accumulative frequency \textit{(distribution)} for each value", font_size=33)
        array_info.center()
        self.wait(1)
        self.play(FadeIn(array_info))
        self.wait(2)
        self.play(FadeOut(array_info))
        self.wait(1)
        #self.play(arr.animate.shift(1* UP+ 1.2* LEFT))
        myF = Tex(r"The \textit{frequency} and \textit{distribution} arrays are as follows", font_size = 35)
        myF = myF.next_to(arr,DOWN)
        self.play(FadeIn(myF), )
        self.wait(1)
        #self.play(myF.animate.shift(1.5* UP+2* LEFT), arr.animate.shift(-1* UP+ -1.2* LEFT))
        self.play(FadeOut(myF))
        labels = Tex(*[
           *[1, 3, 2]
        ])
        labels2 = Tex(*[
           *[1, 4, 6]
        ])
        text = Tex(*[11, 12, 13])
        # space it out
        text.arrange(RIGHT,buff=0.8)
     
        for label2,label,t in zip(labels2,labels,text): 
            label.scale(0.7)
            label.next_to(t,DOWN,buff=0.7)
            label2.scale(0.7)           
            label2.next_to(label,DOWN,buff=0.7)

        up_and_down_line = self.get_up_and_down_line(
            VGroup(text,labels,labels2),
            buff=0.7, # Distance between numbers and lines
            scale=1.4 # Scale of the line
        )
        array_inf = Tex(r" \vspace{0.3cm} \textit{Frequency}: \\ \vspace{0.4cm}\textit{Distribution}:", font_size = 35)
        array_inf.next_to(VGroup(labels,labels2),LEFT * 1.2)
      
        self.play(
            *list(map(lambda x: Write(x,run_time=2),[text,labels,labels2])),
            *list(map(GrowFromCenter,up_and_down_line)),
            Write(array_inf)
        )
        self.wait(2)
        array_in = Tex(
            r"Note that the distribution values indicate the \textbf{proper} positions for the last occurrences of their elements in the \textbf{final} sorted array.",
            font_size= 25
        )        
        array_in.next_to(VGroup(text,labels,labels2,up_and_down_line), 2* UP)
        array_in.scale(1.5)

        self.play(Write(array_in))
        self.wait(1)
        self.play(
            Indicate(labels2[0],scale_factor=2,color=YELLOW,rate_func=there_and_back), Indicate(labels2[1],scale_factor=2,color=YELLOW,rate_func=there_and_back),
            Indicate(labels2[2],scale_factor=2,color=YELLOW,rate_func=there_and_back)
            )
        arr2 = MArray(
             self,
            [1,4,6],
            mob_square_args={'fill_color': BLACK,'color': BLUE_C},
            mob_value_args={'color': WHITE,'font_size':28},
            mob_index_args={'color': WHITE},
            mob_arr_label_args={'color': WHITE},
            label="Distribution",
            hide_index= True
        ) 
  
        arr2= arr2.center()
        self.wait(2)
        self.play(
            FadeOut(array_in),
            FadeTransform(VGroup(array_inf,up_and_down_line,text,labels,labels2),arr2)
        )
        self.wait(2)
        arr.__hide_index = False
        arr = arr.scale(0.8)
        self.play(FadeOut(arr2))
        rules_text = r"\begin{align*}" \
             r"D & = \text{Distribution Array} \\" \
             r"A & = \text{Original Array} \\" \
             r"S & = \text{Sorted Array} \\" \
             r"\end{align*}" 
        yousee = Tex(
            r"We should be able to take advantage of this additional information about values to be sorted", font_size=35
        )

        yousee2 = Tex(
              
             r"For our example, the last element in the array is 12, and, since its distribution value is 4, "
                r"we place this 12 in position $4 - 1 = 3$ of the array $S$ that will hold the sorted list. "
             r"Then we decrease the 12’s distribution value by 1 and proceed to the next (from the right) element in the given array.",
         font_size=35
        )

        Rules = Tex(rules_text, font_size=38)
        code = '''for i in range(n - 1, l, u):
            j = A[i] - l
            S[D[j] - 1] = A[i]
            D[j] -= 1
        return S
        '''
        rendered_code = Code(code=code, tab_width=1, background="rectangle",background_stroke_width=0,background_stroke_color=BLACK,
                            language="Python", font="Monospace", insert_line_no= False, style= Code.styles_list[6], font_size=25)
       
    
        yousee.next_to(Rules, UP)
        yousee2.next_to(yousee,DOWN)
        rendered_code.next_to(Rules, DOWN)
        rendered_code.scale(0.84)
        Rules.center()
        
        self.play(FadeIn(yousee))
        self.play(Write(yousee2,rate_func=smoothstep))
        self.wait(7)
        self.play(FadeOut(yousee),FadeOut(yousee2))
        self.play(Write(Rules))
        self.play(FadeIn(rendered_code))
        self.wait(3)
    



        
 

        arr2 = MArray(
             self,
            [1,4,6],
            mob_square_args={'fill_color': BLACK,'color': BLUE_C},
            mob_value_args={'color': WHITE,'font_size':28},
            mob_index_args={'color': GOLD_A},
            mob_arr_label_args={'color': WHITE,'slant': ITALIC},
            label="D",
            hide_index= True
        ) 
        
        arr.next_to(arr2, UP * 5.1)
        arr.shift(RIGHT * 2.5)
        arr2.next_to(arr, 3* DOWN )
        
        self.play(Rules.animate.scale(0.7).next_to(arr, 4 * LEFT + 0.001*DOWN))
        self.play(rendered_code.animate.scale(0.85).next_to(Rules, (DOWN)))
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=RED_C,buff=5.5,stroke_width=6,max_tip_length_to_length_ratio=0.05) 
        arrow_1.scale(0.4)  
        arrow_1.align_to(rendered_code, 0.3* RIGHT+ 0.003* UP)  
        arrow_1.shift(0.001* UP)
        var = MVariable(self, ' ', label='S[D[j] - 1]',mob_label_args={'font_size': 38,'color':WHITE,'slant': ITALIC},mob_square_args={'fill_color': BLUE_E,'color': WHITE})
        vj = MVariable(self, ' ', label='D[j]',mob_label_args={'font_size': 38,'color':WHITE,'slant': ITALIC},mob_square_args={'fill_color': BLUE_E,'color': WHITE})
        var.next_to(rendered_code, DOWN)
        var.scale(0.7)

        vj.next_to(var,DOWN)
        vj.scale(0.7)
        vj.shift(0.5*RIGHT)
        arr2.shift(0.5*RIGHT)
        arr.shift(0.5*RIGHT)
        self.play(
            Create(arrow_1),
            arr2.animate.shift(3* RIGHT),
            arr2.animate.scale(0.9)
        )
        self.play(arrow_1.animate.shift(0.49 * DOWN + 0.1 * LEFT))
        arr3 = MArray(
             self,      
            [' ', ' ', ' ', ' ', ' ', ' '], 
            mob_square_args={'fill_color': GREEN_E,'color': WHITE},
            mob_value_args={'color': WHITE,'font_size':28},
            mob_index_args={'color': WHITE},
            mob_arr_label_args={'color': WHITE,'slant': ITALIC},
            label="S",
            hide_index= False
        ) 
        

        arr3.scale(0.7) 
        arr3.next_to(arr2, DOWN * 4)
        
        self.play(Create(arr),Create(var),Create(arr3))
        self.wait(2)
        p_i = MArrayPointer(self, arr, 5, 'i', mob_arrow_args={'color': GREEN},
                            mob_label_args={'color': GREEN,'font_size':20}, pointer_pos=MArrayDirection.UP,arrow_gap=0.15,label_gap=0.15,arrow_len=0.4)
        p_j = MArrayPointer(self, arr2, 0, 'j', mob_arrow_args={'color': YELLOW,'stroke_width':7},
                             mob_label_args={'color': YELLOW,'font_size':16},pointer_pos=MArrayDirection.UP,arrow_gap=0.1,label_gap=0.1,arrow_len=0.25)
        self.play(Create(p_i), Create(p_j))
        self.wait(1)
        
       
        # Algorithm: Distribution Counting Sort
        # This code could have been more dynamic but it would have required insanely more time to get the 
        #calculations right, and since it took me 78 Hours to do this, no more time was available.



        #-------------------First iteration Begin --------------------
        p_j.shift_to_elem(1)
        self.wait(1)
        self.play(arrow_1.animate.shift(0.25 * DOWN + 0.1*LEFT ))
        # vj.update_value(
        #         value=arr2.fetch_arr()[1],play_anim=True,
        #         update_anim=Indicate,
        #         update_anim_args={'rate_func': there_and_back,'color': RED_E},
        #      mob_value_args={'font_size': 27}
        #     )
        var.update_value(
                value=arr.fetch_arr()[5],play_anim=True,
                update_anim=Indicate,
                update_anim_args={'rate_func': there_and_back,'color': PURE_RED},
             mob_value_args={'font_size': 27}
            )
        
        
        arr3.update_elem_value(3, 12)
        self.wait(1)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        arr2.update_elem_value(1, 3,update_anim_args={'stroke_color': RED_E})
        
        
        #-------------------First iteration end --------------------
        p_i.shift_to_elem(4)
        self.play(arrow_1.animate.shift(0.55 * UP ))

        self.wait(1)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        var.update_value(
                value=arr.fetch_arr()[4],play_anim=True,
                update_anim=Indicate,
                update_anim_args={'rate_func': there_and_back,'color': PURE_RED},
             mob_value_args={'font_size': 27}
            )
        arr3.update_elem_value(2, 12)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        arr2.update_elem_value(1, 2,update_anim_args={'stroke_color': RED_C})
        
        #-------------------Second iteration end ------------------
        p_i.shift_to_elem(3)
        self.play(arrow_1.animate.shift(0.50 * UP  ))
        
        self.wait(1)
        p_j.shift_to_elem(2)
        
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        var.update_value(
                value=arr.fetch_arr()[3],play_anim=True,
                update_anim=Indicate,
                update_anim_args={'rate_func': there_and_back,'color': PURE_RED},
             mob_value_args={'font_size': 27}
            )
        arr3.update_elem_value(5, 13)
        self.play(arrow_1.animate.shift(0.30 * DOWN ))
        arr2.update_elem_value(2, 5,update_anim_args={'stroke_color': RED_C})
        #-------------------Third iteration end ------------------
        p_i.shift_to_elem(2)
        self.play(arrow_1.animate.shift(0.45 * UP  ))
       
        self.wait(1)
        p_j.shift_to_elem(1)
   
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        var.update_value(
                value=arr.fetch_arr()[2],play_anim=True,
                update_anim=Indicate,
                update_anim_args={'rate_func': there_and_back,'color': PURE_RED},
             mob_value_args={'font_size': 27}
            )
        arr3.update_elem_value(1, 12)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        arr2.update_elem_value(1, 1,update_anim_args={'stroke_color': RED_C})
        
      #-------------------Fourth iteration end ------------------
        p_i.shift_to_elem(1)
        self.play(arrow_1.animate.shift(0.50 * UP  ))
  
        self.wait(1)
        p_j.shift_to_elem(0)
        
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        var.update_value(
                value=arr.fetch_arr()[1],play_anim=True,
                update_anim=Indicate,
                update_anim_args={'rate_func': there_and_back,'color': PURE_RED},
             mob_value_args={'font_size': 27}
            )
        arr3.update_elem_value(0, 11)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        arr2.update_elem_value(0, 0,update_anim_args={'stroke_color': PURE_RED})
        #-------------------FIFTH iteration end ------------------
        p_i.shift_to_elem(0)
        self.play(arrow_1.animate.shift(0.50 * UP  ))
        self.wait(1)
        p_j.shift_to_elem(2)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        var.update_value(
                value=arr.fetch_arr()[0],play_anim=True,
                update_anim=Indicate,
                update_anim_args={'rate_func': there_and_back,'color': PURE_RED},
             mob_value_args={'font_size': 27}
            )
        arr3.update_elem_value(4, 13)
        self.play(arrow_1.animate.shift(0.25 * DOWN ))
        arr2.update_elem_value(2,4,update_anim_args={'stroke_color': PURE_RED})
        
        
        
        self.play(FadeOut(VGroup(arr2,arr,p_j,var,p_i,arr3,arrow_1,Rules,rendered_code)))
        self.wait(3)

        time_complexity_text = Text("Time Complexity Analysis",font_size=35)
        self.play(FadeIn(time_complexity_text))
        self.wait(2)
        self.play(FadeOut(time_complexity_text))
        
        equation = MathTex("c(n) = \sum_{i=1}^{n} 1").scale(1.5)
        equation.center()
        self.play(Write(equation))
   
        time_complexity_analysis = MathTex(
            r"\text{The algorithm performs two passes through the input array.} \\",
            r"\text{Each pass involves linear-time operations (looping through the array once).}"
         ).scale(0.7)
        # Centering the Time Complexity Analysis
        time_complexity_analysis.arrange(DOWN, center=True)
        self.play(equation.animate.shift(UP*0.9).scale(0.7))
        time_complexity_analysis.next_to(equation, 1.5*DOWN)
      
        self.play(Write(time_complexity_analysis))
        self.wait(3)
        self.play(FadeOut(time_complexity_analysis))
        
       

        self.camera.background_color = BLACK
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 10, 1],
            tips=False,
            y_axis_config={"color": WHITE},
            x_axis_config={"color": WHITE},
            axis_config={"color": BLACK, "include_numbers": True,
                              'decimal_number_config' : {
                    'num_decimal_places' : 0,
                    'color' : BLACK
                }},
        )
        labels = ax.get_axis_labels(x_label='time', y_label='input').set_color(YELLOW_D)
        self.play(FadeTransform(equation,ax))
        # Create a linear function
        linear_function = ax.plot(lambda x: x, x_range=[0.001, 10],use_smoothing=False,use_vectorized=True).set_color(BLUE_C)
        linear_function_label = ax.get_graph_label(linear_function, direction= DOWN,label='O(n)').set_color(GREEN_C)
        
        # Add axes and function to the scene
        self.play(FadeIn(labels), Create(linear_function), FadeIn(linear_function_label))
        self.wait(6)
        self.play(FadeOut(ax), FadeOut(linear_function), FadeOut(linear_function_label), FadeOut(labels))



        time_complexity_analysis = MathTex(    
               r"\text{Hence, the overall time complexity is } O(n), \text{ where } n \text{ is the size of the input array.}"
      
         ).scale(0.7)
        time_complexity_analysis.next_to(equation, 1.5*DOWN)
        self.play(FadeIn(time_complexity_analysis))
        self.wait(3)
        self.play(FadeOut(time_complexity_analysis))
        
        self.wait(4)
        title = Tex(r"\textbf{Distribution Counting Sort}", font_size=49).center()
        author = Tex(r"\texttt{Developed By Ashraf Hany}", font_size=19, color=WHITE)
        author.next_to(title, DOWN)
        self.play(FadeIn(title), FadeIn(author))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(author))

        # Credits content
        credits_info = [
            ("Music", "Idea 22 by Gibran Alcocer"),
            ("Used Technologies", "Manim, Numpy, Python"),
            ("Hours Spent to Develop Project", "78")
        ]
        shapes = [
            Circle(color=RED).shift(UP),
            Square(color=GREEN).shift(DOWN),
            Triangle(color=GOLD_B).shift(RIGHT)
        ]

        # Ensure there are equal numbers of credits and shapes
        assert len(credits_info) == len(shapes), "Number of credits and shapes must be equal"
        for i, ((credit_title, credit_content), shape) in enumerate(zip(credits_info, shapes)):
            # Create text for the credits
            credit_title_text = Tex(f"{credit_title}: ", font_size=39, color=BLUE_C)
            credit_content_text = Tex(f"{credit_content}", font_size=36, color=WHITE)
            credit_content_text.next_to(credit_title_text, RIGHT)
            shape.next_to(credit_content_text, DOWN + LEFT)

            circle = Circle()
            circle.set_fill(BLUE, opacity=0.5)
            circle.set_stroke(BLUE_E, width=4)
            circle.next_to(credit_content_text, UP + LEFT)
            circle.scale(0.3)

            square = Square()
            square.scale(0.5)
            if i == 1:
                self.play(FadeIn(credit_title_text), FadeIn(credit_content_text), run_time=1)
                self.play(Create(square))
                self.play(ReplacementTransform(square, circle))
                self.play(Create(shape))
            else:
                self.play(Create(shape))
                self.play(Create(square))
                self.play(ReplacementTransform(square, circle))
                self.play(FadeIn(credit_title_text), FadeIn(credit_content_text), run_time=1)
            self.wait()
            self.play(circle.animate.stretch(4, 0))
            self.play(Rotate(circle, 90 * DEGREES))
            self.play(circle.animate.shift(2 * RIGHT).scale(0.25))
            self.wait(2)
            self.play(FadeOut(circle), FadeOut(shape), FadeOut(credit_title_text), FadeOut(credit_content_text), run_time=1)


    def get_long_line(self,mob,y_direction,buff=0.5,scale=1):
        return Line(
            mob.get_corner(y_direction + LEFT), 
            mob.get_corner(y_direction + RIGHT)
        ).shift(y_direction*buff).scale(scale)

    def get_up_and_down_line(self,mob,**kwargs):
        return VGroup(
            self.get_long_line(mob,UP,**kwargs),
            self.get_long_line(mob,DOWN,**kwargs)
        )        




      

