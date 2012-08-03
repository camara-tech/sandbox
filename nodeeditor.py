# node editor
# requires PyYAML, stackless python, and graphics.py
import graphics
import yaml


def main():
    window = graphics.GraphWin('Generic Node Editor', 800, 600, autoflush=False)
    
    c=graphics.Circle(graphics.Point(300,400),100)
    c.draw(window)
    window.getMouse()
    window.close()
    graphics.update()
    
main()
