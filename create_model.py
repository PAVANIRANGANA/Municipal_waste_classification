from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import Adam

# Load VGG16 base model
vgg_base = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
vgg_base.trainable = False  # Freeze the base layers

# Build the new model on top of VGG16
model = Sequential([
    vgg_base,
    Flatten(),
    Dense(128, activation='relu'),
    Dense(2, activation='softmax')  # 2 output classes
])

# Compile model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Save model to compatible .h5 format
model.save("vgg16.h5")

print("✅ Model saved as vgg16.h5 successfully.")
