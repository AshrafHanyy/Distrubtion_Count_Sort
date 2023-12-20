from manim import *
from manim_data_structures import *
class DistributionCountingSortT(Scene):
    def construct(self):
        time_complexity_text = Text("Time Complexity Analysis",font_size=35)
        self.play(FadeIn(time_complexity_text))
        self.wait(2)
        self.play(FadeOut(time_complexity_text))
        
        equation = MathTex("c(n) = \sum_{i=1}^{n} 1").scale(1.5)
        equation.center()
        self.play(Write(equation))
        self.wait()
        equation.shift(UP * 0.5)

        time_complexity_analysis = MathTex(
            r"\text{The algorithm performs two passes through the input array.} \\",
            r"\text{Each pass involves linear-time operations (looping through the array once).} \\",
            r"\text{Hence, the overall time complexity is } O(n), \text{ where } n \text{ is the size of the input array.}"
        ).scale(0.7)

        # Centering the Time Complexity Analysis
        time_complexity_analysis.arrange(DOWN, center=True)
        

        self.play(equation.animate.shift(UP*0.7).scale(0.7))
        self.wait(5)
        time_complexity_analysis.next_to(equation, 1.5*DOWN)
      
        self.play(FadeIn(time_complexity_analysis))
        self.wait(5)



      





