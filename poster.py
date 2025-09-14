from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas setup
width, height = 1000, 1000
poster = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(poster)

# Gradient background (pink → black)
top_color = (255, 20, 147)   # hot pink
bottom_color = (0, 0, 0)     # black

for y in range(height):
    blend = y / height
    r = int(top_color[0] * (1 - blend) + bottom_color[0] * blend)
    g = int(top_color[1] * (1 - blend) + bottom_color[1] * blend)
    b = int(top_color[2] * (1 - blend) + bottom_color[2] * blend)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Fonts
font_big = ImageFont.truetype("Orbitron-Bold.ttf", 80)
font_small = ImageFont.truetype("Orbitron-Bold.ttf", 40)


# Function to add glow to text
def draw_glow_text(draw, position, text, font, text_color, glow_color, blur_radius=8):
    temp = Image.new("RGBA", poster.size, (0, 0, 0, 0))
    temp_draw = ImageDraw.Draw(temp)
    temp_draw.text(position, text, font=font, fill=glow_color)
    blurred = temp.filter(ImageFilter.GaussianBlur(blur_radius))
    poster.paste(blurred, (0, 0), blurred)
    draw.text(position, text, font=font, fill=text_color)

# Title (pink glow)
title = "CCIS PHANTOMS"
title_bbox = draw.textbbox((0, 0), title, font=font_big)
title_w, title_h = title_bbox[2] - title_bbox[0], title_bbox[3] - title_bbox[1]
title_pos = ((width - title_w) // 2, 50)
draw_glow_text(draw, title_pos, title, font_big, (255, 255, 255), (255, 20, 147))

# Subtitle (white glow)
subtitle = "A DREAM, A THOUGHT, A REALITY"
sub_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
sub_w, sub_h = sub_bbox[2] - sub_bbox[0], sub_bbox[3] - sub_bbox[1]
sub_pos = ((width - sub_w) // 2, 150)
draw_glow_text(draw, sub_pos, subtitle, font_small, (255, 255, 255), (255, 255, 255))

# Insert Mascot Image
mascot = Image.open("Screenshot_2025-09-14_140957-removebg-preview (2).png")
mascot = mascot.convert("RGBA")
mascot = mascot.resize((550, 550))

# Mascot glow (pink aura)
glow = Image.new("RGBA", poster.size, (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)
mascot_x = (width - mascot.width) // 2
mascot_y = (height - mascot.height) // 2 - 45
glow_draw.ellipse([mascot_x-20, mascot_y-20, mascot_x+mascot.width+20, mascot_y+mascot.height+20], fill=(255, 20, 147, 180))
glow = glow.filter(ImageFilter.GaussianBlur(40))
poster.paste(glow, (0, 0), glow)

# Paste mascot
poster.paste(mascot, (mascot_x, mascot_y), mascot)

# Slogan (gold glow)
slogan = "UNITE. COMPETE. CONQUER."
slogan_bbox = draw.textbbox((0, 0), slogan, font=font_small)
slogan_w, slogan_h = slogan_bbox[2] - slogan_bbox[0], slogan_bbox[3] - slogan_bbox[1]
slogan_pos = ((width - slogan_w) // 2, height - 120)
draw_glow_text(draw, slogan_pos, slogan, font_small, (255, 255, 255), (255, 215, 0))

# Multi-colored slogan
slogan_parts = [
    ("UNITE.", (0, 191, 255), (135, 206, 250)),    # Red text, light red glow  
    (" COMPETE.", (0, 255, 0), (100, 255, 100)),   # Green text, light green glow
    (" CONQUER.", (255, 0, 0), (255, 100, 100))    # Blue text, light blue glow
]

# Measure full slogan width
total_w = 0
max_h = 0
for word, _, _ in slogan_parts:
    bbox = draw.textbbox((0, 0), word, font=font_small)
    total_w += bbox[2] - bbox[0]
    max_h = max(max_h, bbox[3] - bbox[1])

# Starting position (centered)
x = (width - total_w) // 2
y = height - 120

# Draw each part with its own color & glow
for word, text_color, glow_color in slogan_parts:
    bbox = draw.textbbox((0, 0), word, font=font_small)
    w = bbox[2] - bbox[0]
    draw_glow_text(draw, (x, y), word, font_small, text_color, glow_color, blur_radius=10)
    x += w


# Save & Show
poster.save("PPROFELEC2_4_MendezJoseKim_Activity1.png")
poster.show()
