from manim import *

class FusingText(Scene):
    def construct(self):
        # 1. Create the final word
        word = Text("FUSING", font_size=96)
        
        # 2. Create individual letters scattered around the screen
        # We use a VGroup (Vector Group) to handle them easily
        letters = VGroup(*[Text(char, font_size=96) for char in "FUSING"])
        
        # Randomly position letters away from the center
        import random
        for letter in letters:
            letter.move_to([random.uniform(-5, 5), random.uniform(-3, 3), 0])
            letter.set_color(interpolate_color(BLUE, WHITE, random.random()))

        # 3. The Animation Sequence
        self.play(FadeIn(letters, shift=UP))
        self.wait(0.5)

        # "Fuse" the scattered letters into the final word positions
        self.play(
            ReplacementTransform(letters, word),
            word.animate.set_color(RED),
            run_time=2,
            rate_func=slow_into
        )
        
        # Add a little glow or scale effect at the end
        self.play(word.animate.scale(1.2), run_time=0.5)
        self.play(word.animate.scale(1/1.2), run_time=0.5)
        self.wait(2)