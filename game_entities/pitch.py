import pygame
from constants import (WINDOW_HEIGHT, WINDOW_WIDTH, 
                       BAR_COLOR, BORDER_SIZE)


class Pitch(object):
    
    @classmethod
    def draw_border(self, surface):
        # Draw borders around the screen
        pygame.draw.rect(surface, BAR_COLOR, ((0, 0), (WINDOW_WIDTH, BORDER_SIZE)))  # Top border
        pygame.draw.rect(surface, BAR_COLOR, ((0, 0), (BORDER_SIZE, WINDOW_HEIGHT)))  # Left border
        pygame.draw.rect(surface, BAR_COLOR, ((0, WINDOW_HEIGHT - BORDER_SIZE), (WINDOW_WIDTH, BORDER_SIZE)))  # Bottom border
        pygame.draw.rect(surface, BAR_COLOR, ((WINDOW_WIDTH - BORDER_SIZE, 0), (BORDER_SIZE, WINDOW_HEIGHT)))  # Right border

    @classmethod
    def draw_separator(self, surface):
        pygame.draw.line(surface, BAR_COLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), BORDER_SIZE)
    
    @classmethod
    def draw_background(self, surface):
        gradient_color_start = (0, 0, 0)      # Darker shade
        gradient_color_end = (150, 0, 180)    # Lighter shade

        for y in range(WINDOW_HEIGHT):
            # Interpolate between the start and end colors based on the vertical position
            gradient_color = (
                int(gradient_color_start[0] + (gradient_color_end[0] - gradient_color_start[0]) * (y / WINDOW_HEIGHT)),
                int(gradient_color_start[1] + (gradient_color_end[1] - gradient_color_start[1]) * (y / WINDOW_HEIGHT)),
                int(gradient_color_start[2] + (gradient_color_end[2] - gradient_color_start[2]) * (y / WINDOW_HEIGHT))
            )
            pygame.draw.rect(surface, gradient_color, (0, y, WINDOW_WIDTH, 1))
        
    @classmethod
    def draw(self, surface):
        self.draw_background(surface)
        self.draw_separator(surface)
        self.draw_border(surface)
