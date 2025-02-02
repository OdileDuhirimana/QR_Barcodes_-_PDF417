import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Load the Aztec code image
image_path = "./image05.jpg"
image = cv2.imread(image_path)

# Decode the Aztec code using pyzbar
barcodes = decode(image)
for barcode in barcodes:
    data = barcode.data.decode("utf-8")
    print(f"Decoded Data: {data}")  # Print the decoded data to the terminal
    
    # Get the points for the bounding box
    points = barcode.polygon
    points = [(point.x, point.y) for point in points]
    
    # Draw the bounding box in a bright color (e.g., blue)
    cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (255, 0, 0), 3)
    
    # Add the decoded text (with a contrasting color, e.g., yellow) next to the box
    x, y = points[0]  # Get the top-left corner for text positioning
    cv2.putText(image, data, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)  # Yellow text, larger size

# Display the image with the Aztec code highlighted and annotated
cv2.imshow("Aztec Code with Annotation", image)

# Wait for a key press and capture the pressed key
key = cv2.waitKey(0)

if key == ord('q'):  # Close window if the 'q' key is pressed
    cv2.destroyAllWindows()

# Save the annotated image
output_file = "decoded_aztec.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")  # Print where the image was saved
