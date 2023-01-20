from flask import Flask, render_template, Response
import pygame
import random

app = Flask(__name__)

@app.route("/")
def index():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Pygame Memory Test on Flask")

    # Initialize the game variables
    cards = ["apple", "banana", "orange", "strawberry"] * 2
    random.shuffle(cards)
    current_card = None
    cards_left = len(cards)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if cards_left > 0:
            # Draw the current card
            if current_card:
                font = pygame.font.Font(None, 36)
                text = font.render(current_card, True, (255, 255, 255))
                screen.blit(text, (200, 150))

            # Handle user input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                current_card = cards.pop()
                cards_left -= 1

            elif keys[pygame.K_RETURN]:
                if current_card in cards:
                    cards.remove(current_card)
                    score += 1
                else:
                    score -= 1
                current_card = None

            # Draw the score
            font = pygame.font.Font(None, 36)
            text = font.render("Score: " + str(score), True, (255, 255, 255))
            screen.blit(text, (5, 5))

        else:
            # Game over
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over!", True, (255, 255, 255))
            screen.blit(text, (150, 150))

        pygame.display.flip()

        # Create a surface with the current Pygame screen
        surface = pygame.surfarray.make_surface(pygame.surfarray.pixels3d(screen))

        # Encode the surface as a PNG image
        image_data = pygame.image.tostring(surface, 'RGB')

        # Stream the image data to the browser
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + image_data + b'\r\n\r\n')

    pygame.quit()

@app.route("/video_feed")
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(index(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)