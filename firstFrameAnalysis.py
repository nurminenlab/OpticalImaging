# average frames over trials, let's call the resulting times series X
# sum X over time in 1 second bins
# subtract 1 second of baseline from X, lets call the result X-b
# compute X-b for both conditions
# filter X-b for both conditions with averaging filter (box car, 5x5)
# subtract filtered X-b
# take average of X-b over time
# (ESD denoising)
# show the resulting image



