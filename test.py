import face_recognition
import cv2

# Load an image of Adam (make sure you have a picture of yourself named 'adampic.jpeg' in the same folder)
# You can update the file path accordingly if your image is elsewhere
known_image = face_recognition.load_image_file("adampic.jpeg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create an array of known face encodings and corresponding names
known_face_encodings = [known_face_encoding]
known_face_names = ["Adam"]

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a single frame from the webcam
    ret, frame = video_capture.read()

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR (OpenCV format) to RGB (face_recognition format)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through all faces detected
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the detected face matches our known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If we have a match, assign the corresponding name
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label it with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

        # If the detected face is Adam's, display "This is Adam" on the screen
        if name == "Adam":
            cv2.putText(frame, "This is Adam", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
