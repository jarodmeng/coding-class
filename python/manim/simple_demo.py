#!/usr/bin/env python3
"""
Simple Manim Demo - No LaTeX Required!
This file shows cool animations that work without LaTeX installation.
"""

from manim import *

class SimpleManimDemo(Scene):
    """
    A simple Manim demo that works without LaTeX!
    
    This shows what kids can create with basic Manim:
    - Beautiful mathematical shapes
    - Smooth animations and transformations
    - Geometric patterns
    - Interactive concepts
    """
    
    def construct(self):
        # Title
        title = Text("🎨 Simple Manim Animations!", 
                    font_size=36, color=BLUE)
        subtitle = Text("No LaTeX Required!", 
                       font_size=24, color=GREEN)
        
        # Show title first
        self.play(Write(title))
        self.wait(1)
        
        # Clear title, then show subtitle
        self.play(FadeOut(title))
        self.wait(0.5)
        self.play(Write(subtitle))
        self.wait(1)
        
        # Clear subtitle completely
        self.play(FadeOut(subtitle))
        self.wait(0.5)  # Ensure clearing is complete
        
        # 1. Beautiful Mathematical Shapes
        self.show_mathematical_shapes()
        
        # Clear screen completely between sections
        self.clear()
        self.wait(0.5)
        
        # 2. Animated Transformations
        self.show_animated_transformations()
        
        # Clear screen completely between sections
        self.clear()
        self.wait(0.5)
        
        # 3. Geometric Patterns
        self.show_geometric_patterns()
        
        # Clear screen completely between sections
        self.clear()
        self.wait(0.5)
        
        # 4. Interactive Concepts
        self.show_interactive_concepts()
        
        # Final message
        self.show_final_message()
    
    def show_mathematical_shapes(self):
        """Show beautiful mathematical shapes with animations."""
        title = Text("1. Beautiful Mathematical Shapes", 
                    font_size=28, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        
        # Clear title before starting animations
        self.play(FadeOut(title))
        self.wait(0.5)
        
        # Create a circle that becomes a square
        circle = Circle(radius=1, color=RED, fill_opacity=0.3)
        square = Square(side_length=2, color=BLUE, fill_opacity=0.3)
        
        self.play(Create(circle))
        self.wait(0.5)
        self.play(Transform(circle, square))
        self.wait(0.5)
        
        # Create a triangle
        triangle = Triangle(color=GREEN, fill_opacity=0.3)
        self.play(Create(triangle))
        self.wait(0.5)
        
        # Animate all shapes
        self.play(
            circle.animate.scale(0.8).shift(LEFT * 2),
            triangle.animate.scale(0.8).shift(RIGHT * 2)
        )
        self.wait(1)
        
        # Clear everything completely
        self.play(FadeOut(circle), FadeOut(triangle))
        self.wait(0.5)  # Small pause to ensure everything is cleared
    
    def show_animated_transformations(self):
        """Show cool transformations and movements."""
        title = Text("2. Animated Transformations", 
                    font_size=28, color=ORANGE)
        self.play(Write(title))
        self.wait(1)
        
        # Clear title before starting animations
        self.play(FadeOut(title))
        self.wait(0.5)
        
        # Create a star that rotates and scales
        star = Star(outer_radius=1, color=PURPLE, fill_opacity=0.5)
        self.play(Create(star))
        
        # Rotate and scale
        self.play(
            star.animate.rotate(PI/2).scale(1.5),
            run_time=2
        )
        self.wait(0.5)
        
        # Move in a circle
        self.play(
            star.animate.move_to(ORIGIN).scale(0.7),
            run_time=1
        )
        
        # Create multiple stars
        stars = VGroup(*[Star(outer_radius=0.3, color=color, fill_opacity=0.6)
                        for color in [RED, GREEN, BLUE, YELLOW, PURPLE]])
        
        for i, star_copy in enumerate(stars):
            star_copy.move_to([np.cos(i * 2*PI/5), np.sin(i * 2*PI/5), 0])
        
        self.play(Create(stars))
        self.wait(0.5)
        
        # Rotate all stars
        self.play(stars.animate.rotate(PI), run_time=2)
        self.wait(1)
        
        # Clear everything completely
        self.play(FadeOut(stars))
        self.wait(0.5)  # Small pause to ensure everything is cleared
    
    def show_geometric_patterns(self):
        """Show beautiful geometric patterns."""
        title = Text("3. Geometric Patterns", 
                    font_size=28, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        
        # Clear title before starting animations
        self.play(FadeOut(title))
        self.wait(0.5)
        
        # Create a spiral pattern
        dots = VGroup()
        for i in range(50):
            angle = i * 0.5
            radius = i * 0.1
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            # Use simple color interpolation
            if i < 25:
                color = interpolate_color(RED, BLUE, i/25)
            else:
                color = interpolate_color(BLUE, RED, (i-25)/25)
            dot = Dot([x, y, 0], color=color)
            dots.add(dot)
        
        self.play(Create(dots), run_time=3)
        self.wait(0.5)
        
        # Clear dots before creating flower pattern
        self.play(FadeOut(dots))
        self.wait(0.5)
        
        # Create a flower pattern
        flower = VGroup()
        for i in range(12):
            color = interpolate_color(PINK, PURPLE, i/12)
            petal = Ellipse(width=0.5, height=2, color=color)
            petal.rotate(i * PI/6)
            flower.add(petal)
        
        self.play(Create(flower))
        self.wait(0.5)
        
        # Rotate the flower
        self.play(flower.animate.rotate(PI), run_time=2)
        self.wait(1)
        
        # Clear everything completely
        self.play(FadeOut(dots), FadeOut(flower))
        self.wait(0.5)  # Small pause to ensure everything is cleared
    
    def show_interactive_concepts(self):
        """Show interactive mathematical concepts."""
        title = Text("4. Interactive Mathematical Concepts", 
                    font_size=28, color=GOLD)
        self.play(Write(title))
        self.wait(1)
        
        # Clear title before starting animations
        self.play(FadeOut(title))
        self.wait(0.5)
        
        # Create a clear fraction visualization
        fraction_text = Text("3/4", font_size=48, color=YELLOW)
        self.play(Write(fraction_text))
        self.wait(0.5)
        
        # Create a rectangle centered on screen
        rectangle = Rectangle(width=6, height=2, color=BLUE, fill_opacity=0.3)
        rectangle.move_to(ORIGIN + DOWN * 1.5)  # Position below center
        
        # Create division lines to show 4 equal parts
        lines = VGroup()
        for i in range(1, 4):
            x_pos = rectangle.get_left()[0] + (i * rectangle.width / 4)
            line = Line(
                [x_pos, rectangle.get_top()[1], 0],
                [x_pos, rectangle.get_bottom()[1], 0],
                color=WHITE, stroke_width=3
            )
            lines.add(line)
        
        # Show the rectangle first
        self.play(Create(rectangle))
        self.wait(0.5)
        
        # Add division lines
        self.play(Create(lines))
        self.wait(0.5)
        
        # Highlight the first 3 parts (3/4)
        highlight = Rectangle(
            width=rectangle.width * 3/4, 
            height=rectangle.height, 
            color=RED, 
            fill_opacity=0.6
        )
        # Position highlight to cover first 3 parts
        highlight.move_to(rectangle.get_left() + [highlight.width/2, 0, 0])
        self.play(Create(highlight))
        
        # Add explanatory text
        explanation = Text("3 out of 4 parts highlighted", 
                          font_size=24, color=WHITE)
        explanation.next_to(rectangle, DOWN, buff=0.5)
        self.play(Write(explanation))
        
        self.wait(1.5)
        
        # Clear everything completely
        self.play(FadeOut(fraction_text), FadeOut(rectangle), 
                 FadeOut(lines), FadeOut(highlight), FadeOut(explanation))
        self.wait(0.5)  # Small pause to ensure everything is cleared
    
    def show_final_message(self):
        """Show final inspiring message."""
        message1 = Text("🎉 You can create ALL of this with Manim!", 
                       font_size=32, color=GREEN)
        message2 = Text("Start with simple shapes, then build up to complex animations!", 
                       font_size=24, color=BLUE)
        message3 = Text("Ready to start your mathematical animation journey?", 
                       font_size=28, color=YELLOW)
        
        # Show first message
        self.play(Write(message1))
        self.wait(1)
        
        # Clear first message, then show second
        self.play(FadeOut(message1))
        self.wait(0.5)
        self.play(Write(message2))
        self.wait(1)
        
        # Clear second message, then show third
        self.play(FadeOut(message2))
        self.wait(0.5)
        self.play(Write(message3))
        self.wait(2)
        
        # Final flourish with the third message
        self.play(
            message3.animate.scale(1.2).set_color(RED),
            run_time=2
        )
        self.wait(2)
        
        # Final clear to end the demo cleanly
        self.play(FadeOut(message3))
        self.wait(1)

# ============================================================================
# HOW TO RUN THIS DEMO
# ============================================================================

if __name__ == "__main__":
    print("🎬 Simple Manim Demo - No LaTeX Required!")
    print("=" * 50)
    print()
    print("This file shows amazing things you can create with Manim!")
    print()
    print("To run this demo:")
    print("1. Activate virtual environment: source manim_env/bin/activate")
    print("2. Run: manim -pql simple_demo.py SimpleManimDemo")
    print()
    print("The -pql flags mean:")
    print("  -p: Preview the animation")
    print("  -q: Medium quality (faster rendering)")
    print("  -l: Use a lower resolution")
    print()
    print("🚀 Get ready to be amazed by mathematical animations!")
    print("💡 You'll learn to create these step by step in future lessons!")
