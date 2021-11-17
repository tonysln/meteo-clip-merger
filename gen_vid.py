#!/usr/bin/env python

from PIL import Image, ImageFont, ImageDraw
import numpy as np
import cv2

temps = []
# Read in the data file and select which categories to use
with open('temps.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        # Skip header row
        if line.startswith('Aeg'): continue	
        
        # Split and select cols (depends on file structure)
        line = line.split(', ')
        temps.append([round(float(line[1]),1), round(float(line[2]),1), 
                    round(float(line[4]),1), line[0]])
    

vid = cv2.VideoCapture('2021-02.mp4')

# Output in MP4, 48 FPS, 1280x1024 (re-check with your source)
# out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID'), 48, (1280,1024))

frm = 1200 # Start at hour 4
idx = 0
while(True):
    _,frame = vid.read()

    # Open as PIL img
    im = Image.fromarray(frame)
    draw = ImageDraw.Draw(im)

    # Load fonts
    font_file = '/Library/Fonts/LucidaGrande.ttc'
    mono1 = ImageFont.truetype(font_file, 36)
    mono2 = ImageFont.truetype(font_file, 31)
        
    # Draw text (with bg)
    dt = temps[frm][3]
    txt = f'RH: {temps[frm][1]}%'
    txt = dt.split()[1]
    
    draw.rectangle((900, 954, 1280, 1024), fill=(0,0,0), outline=(0,0,0))
    draw.text((914, 968), f'{temps[frm][0]}°C', (255,255,255), 
                        font=mono1, stroke_width=2, stroke_fill=(0,0,0))
    draw.text((1102, 972), txt, (220,220,220), 
                        font=mono2, stroke_width=2, stroke_fill=(0,0,0))

    # Back to cv2 image
    frame_2 = np.array(im)
    
    # Save
# 	out.write(frame_2)
    
    # Display frame
    cv2.imshow('video', frame_2)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Match readings with the video
    # 1 sec/frame vs 1 measurement/5 secs
    idx += 1
    if idx == 5:
        frm += 1
        idx = 0
  

vid.release()
# out.release()
cv2.destroyAllWindows()
