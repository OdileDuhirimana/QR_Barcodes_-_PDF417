from pylibdmtx.pylibdmtx import decode
import cv2
import numpy as np

# Read image (ensure the image exists)
image = cv2.imread("./image02.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found.")
    exit()

# Decode DataMatrix code from the image
decoded_objects = decode(image)

# If no objects are decoded, display a message
if not decoded_objects:
    print("No DataMatrix code detected.")
else:
    # Print and annotate decoded data
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        print("Decoded Data:", data)

        # Ensure the points are in the correct numpy format for polylines
        points = np.array(obj.rect, dtype=np.int32)

        # Reshape the points into the correct format for polylines
        points = points.reshape((-1, 1, 2))

        # Annotate the image with the DataMatrix's rectangle
        cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

        # Draw the decoded text on the image
        cv2.putText(image, data, (points[0][0][0], points[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save the annotated image
output_file = "decoded_datamatrix_code.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")

# Display the annotated image
cv2.imshow("Barcode with Annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
