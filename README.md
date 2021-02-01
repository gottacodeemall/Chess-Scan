# Chess Scan
Generate and update the FEN notation of a live chess game on the go with no human intervention and only a single camera.

## Chess Scan Backend
This repo covers the Deep Learning part of this project where the video from the live stream is fed into the system and the resulting images are further used to generate the board position at that point in time.

## Approach
- To make it work for a single camera approach, we decided to incline the camera at a 60 degree incline.
	- A horizontal capture would result in pieces blocking each other.
	- A vertical capture does yield great result as the pieces look the same from above.
- The captured image is broken down into 64 individual squares for piece recognition at that particular square.
	- We decided that the width of each square remains the same but the height to be captured decreases as we go from the nearest to farthest square from the camera.
			- This was decided as the pieces appear larger if they are closer to the camera.
- Once the inferences are made against each square. The inferred pieces can mapped to their squares and the FEN notation can be generated at this instance in time.

## CNN and Training
-  **CNN**: Faster RCNN Inception V2 trained on COC 2018.
- Used Sobel Edge Detection to capture the location of the board and further used point detection to get the locations of each individual square from which cropped images were extracted.
