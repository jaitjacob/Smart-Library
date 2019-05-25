import cv2
import os
import argparse
from imutils import paths
import face_recognition
import pickle
from imutils.video import VideoStream
import face_recognition
import imutils
import pickle
import time


class FaceID:
    def __init__(self):
        self.data_folder = "./Face-ID/dataset/"
        self.data_file = self.data_folder + "encodings.pickle"
        self.data = pickle.loads(open(self.encodings_file, "rb").read())

        self.detection_method = "hog"

        self.resolution = 240

        # Create a new folder for the new name
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def register_user(self, username: str):
        folder = self.data_folder + username


        # Create a new folder for the new name
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Start the camera
        cam = cv2.VideoCapture(0)
        # Set video width
        cam.set(3, 1280)
        # Set video height
        cam.set(4, 720)
        # Get the pre-built classifier that had been trained on 3 million faces
        face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        img_counter = 0
        while img_counter <= 10:
            key = input("Press q to quit or ENTER to continue: ")
            if key == "q":
                break

            ret, frame = cam.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            if (len(faces) == 0):
                print("No face detected, please try again")
                continue

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                img_name = "{}/{:04}.jpg".format(folder, img_counter)
                cv2.imwrite(img_name, frame[y: y + h, x: x + w])
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        self.encode_images(username)

    def encode_images(self, username: str):
        folder = self.data_folder + username

        # grab the paths to the input images in our dataset
        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images(folder))

        # initialize the list of known encodings and known names
        knownEncodings = self.data["encodings"]
        knownNames = self.data["names"]

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))


            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb, model=self.detection_method)

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and encodings
                knownEncodings.append(encoding)
                knownNames.append(username)

        # dump the facial encodings + names to disk
        print("[INFO] serializing encodings...")

        data = {"encodings": knownEncodings, "names": knownNames}

        with open(self.data_file, "wb") as f:
            f.write(pickle.dumps(data))

    def recognize_user(self):

        # load the known faces and embeddings
        print("[INFO] loading encodings...")

        # initialize the video stream and then allow the camera sensor to warm up
        print("[INFO] starting video stream...")
        vs = VideoStream(src=0).start()
        time.sleep(2.0)

        # loop over frames from the video file stream
        for i in range(3):
            # grab the frame from the threaded video stream
            frame = vs.read()

            # convert the input frame from BGR to RGB then resize it to have
            # a width of 750px (to speedup processing)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=self.resolution)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input frame, then compute
            # the facial embeddings for each face
            boxes = face_recognition.face_locations(rgb, model=self.detection_method)
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known
                # encodings
                matches = face_recognition.compare_faces(self.data["encodings"], encoding)
                name = "Unknown"

                # check to see if we have found a match
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        name = self.data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    # determine the recognized face with the largest number
                    # of votes (note: in the event of an unlikely tie Python
                    # will select first entry in the dictionary)
                    name = max(counts, key=counts.get)

                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for name in names:
                if name != "Unknown":
                    # do a bit of cleanup
                    vs.stop()
                    return name


            # Set a flag to sleep the cam for fixed time
            time.sleep(3.0)

        vs.stop()
        return "Unknown"

