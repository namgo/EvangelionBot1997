# What is this?
EVAbot 1.9 + 9.7: You can (not) sentience

I feel that this is a good starting place for a python/cloud☁ tutorial.
Contained here is the source repository and guide for Evangelion Bot.

titles obtained from epguides.com

This isn't really a tutorial yet, but stay tuned.

# Does this cost money?
Google calculator suggests I might be paying at most $1USD/mo for storage, but doesn't do much to take away from the $300 credit.

Processing videos is heavily CPU dependant, but I'd recommend not trying to use cloud resources to do this, otherwise you might end up paying for the time you save.

# Converting videos to screenshots
This does involve some bash scripting.
This will also require a total of about 41.6GB of storage space (between images and video), so be prepared.

Check out the bash script I've included in video_processing.
First we'll navigate to our directory with `cd`.
We'll run `bash EvangelionEpisodeBot1997_location/video_processing/process.sh`.
KEEP IN MIND: This script was made for a very specific Evangelion copy, its filename system will probably not work for you, you'll have to edit it.

This is going to take a few hours, depending on your CPU, since it's transcoding all the videos into images, we're going with bitmaps to save time, and we can encode to .png to save space later.

## Getting rid of the intro/extro
I couldn't think of a programmatic way to do this, so we'll just browse through all 26 episodes and remove the intro/extro images.

# Getting subtitles
You'll only really be able to download 100 or so subs per day unless you can find a work-around.

# Saving money
To save money, we'll store the list of blobs in our firestore database
