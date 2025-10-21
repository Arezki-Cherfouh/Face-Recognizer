import face_recognition
known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_image = face_recognition.load_image_file("test.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([known_encoding], unknown_encoding)
if results[0]:
    print("It's the same person!")
else:
    print("Not the same person.")
