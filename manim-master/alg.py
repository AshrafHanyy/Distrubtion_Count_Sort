from manim import *

class BinaryTreeNode(VGroup):
    def __init__(self, value, height=1, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.height = height


        # Create the circle representing the node
        self.circle = Circle(color=BLUE, radius=0.5)
        self.text = Text(str(value)).scale(0.7)

        # Create the left and right children
        self.left_child = None
        self.right_child = None

        # Create the arrows
        self.left_arrow = Arrow(self.circle.get_bottom(), self.circle.get_top(), color=WHITE)
        self.right_arrow = Arrow(self.circle.get_bottom(), self.circle.get_top(), color=WHITE)

        # Positioning
        if height > 1:
            self.left_child = BinaryTreeNode(value - 1, height=height - 1)
            self.right_child = BinaryTreeNode(value + 1, height=height - 1)
            self.left_arrow.next_to(self.left_child.circle, UP)
            self.right_arrow.next_to(self.right_child.circle, UP)

        self.add(self.circle, self.text)
    def update_balance_factor(self):
        left_height = self.left_child.height if self.left_child else 0
        right_height = self.right_child.height if self.right_child else 0
        self.balance_factor = left_height - right_height
        self.text = Text(f"{self.value}\nBF: {self.balance_factor}").scale(0.7)
        self.remove(self.text)
        self.add(self.text)
    def construct(self):
        if self.left_child:
            self.play(Create(self.left_child), Create(self.right_child))
            self.play(Create(self.left_arrow), Create(self.right_arrow))

class BinaryTreeScene(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        quote = Tex("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = Tex("A person who never made a mistake never tried anything new")
        quote2.set_color(WHITE)
        author=Tex("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))   
        self.play(FadeOut(author))
        tree = BinaryTreeNode(2, height=3)
        self.play(Create(tree))
        self.wait()

        # Scale down the main node
        self.play(tree.animate.shift(UP * 0.8))

        # Add text before introducing child nodes
        avl_text = Text("AVL Trees By Ashraf Hany").scale(0.8)
        avl_text.next_to(tree.circle, DOWN)
        avl_text22 = Text("").scale(0.8)
        avl_text22.next_to(tree.circle, DOWN)
        self.play(FadeIn(avl_text))
        self.wait()
        self.play(FadeOut(avl_text))
      



        # Add two child nodes below the main node
        child1 = BinaryTreeNode(3, height=3)
        child2 = BinaryTreeNode(1, height=3)
        child1.next_to(tree.circle, DOWN + LEFT, buff=1.5)
        child2.next_to(tree.circle, DOWN + RIGHT, buff=1.5)
        arrow1 = Arrow(tree.circle.get_bottom(), child1.circle.get_top(), color=WHITE)
        arrow2 = Arrow(tree.circle.get_bottom(), child2.circle.get_top(), color=WHITE)

        # Connect child nodes with arrows
        self.play(Create(child1), Create(child2))
        self.play(Create(arrow1), Create(arrow2))
        self.wait()
       
        # Group the entire tree (main node + child nodes + arrows)
        entire_tree = VGroup(tree, child1, child2, arrow1, arrow2)

        # Shift the entire tree to the right and upwards
        self.play(FadeOut(entire_tree))
        #self.wait(5)
        avl_text2 = Text("Plotting Functions").scale(0.8)
        self.play(FadeIn(avl_text2))
        self.wait()
        self.play(FadeOut(avl_text2))
        node_list = []
        eq1A = Tex("4x + 3y")
        eq1B = Tex("=")
        eq1C = Tex("0")
        eq2A = Tex("5x -2y")
        eq2B = Tex("=")
        eq2C = Tex("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A,eq2B,eq1B,eq2C,eq1C)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))
        self.wait(2)
        self.play(FadeOut(braces))
        self.play(FadeOut(eq_text))
        self.play(FadeOut(eq_group))
  
        plane_kwargs = self.CONFIG["plane_kwargs"]
        plane = NumberPlane(**plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]     #List of vectors pointing to each grid point

        vec_field = []  #Empty list to use in for loop
       
        field = 2.5*RIGHT + 2.5*UP   #Constant field up and to right
        result = Vector(field)   #Create vector and shift it to grid point
        vec_field.append(result)   #Append to list

        draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup


        self.play(Create(draw_field))   #Draw VGroup on screen

        self.wait(2)
        self.play(Rotate(draw_field, angle=np.pi / 4))  # Adjust the angle as needed
        self.wait(3)
        self.play(FadeOut(draw_field))

        draw_field = VGroup(*vec_field)    
        for i in range(4, 9):
          child = BinaryTreeNode(i, height=4)
          child.next_to(tree.circle, DOWN + LEFT, buff=(len(node_list) * 0.2) + 1.8)  # Adjust the buff value as needed
          node_list.append(child)

         # Connect the new node with an arrow
        arrow = Arrow(tree.circle.get_bottom(), child.circle.get_top(), color=WHITE)
        #self.play(Create(child), Create(arrow))

         # Update balance factors after insertion
        tree.update_balance_factor()
        for node in node_list:
             node.update_balance_factor()

 