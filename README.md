# What is this?
I feel that this is a good starting place for a python/cloud☁ tutorial.
Contained here is the source repository and guide for Evangelion Bot.


# Does this cost money?
Google calculator suggests I might be paying a $1USD/mo or so for storage, but doesn't do much to take away from the $300 credit.

# How long did this take?
I broke up the bot into parts, so generate.py should have taken about an hour if I had prepared the fonts ahead of time instead of trying to see what looked best.

Processing videos is heavily CPU dependant, but I'd recommend not trying to use cloud resources to do this, otherwise you might end up paying for the time you save.

# How is this being done?
Everyting done here is contained within either Windows Subsystem for Linux or a Cloud System, so all commands are for linux. I highly recommend all aspiring botmins get comfortable with WSL.

## How to install WSL
This will not be covered by the tutorial but can be found here:
https://docs.microsoft.com/en-us/windows/wsl/install-win10

# Converting videos to screenshots
This does involve some bash scripting.
This will also require about 41.6GB of storage space, so be prepared.

Check out the bash script I've included in video_processing.
First we'll navigate to our directory with `cd`.
We'll run `bash EvangelionEpisodeBot1997_location/video_processing/process.sh`.

This is going to take a few hours, depending on your CPU, since it's transcoding all the videos into images, we're going with bitmaps to save time, and we can encode to .png to save space later.

## Getting rid of the intro/extro
I couldn't think of a programmatic way to do this, so we'll just browse through all 26 episodes and remove the intro/extro images.

# Getting subtitles
Register for an account on opensubtitles
