import src.logic_scripts.entity as entity
import video_shower
from src.logic_scripts import location
from src.logic_scripts import image_location
import src.video_shower
import enums
from pathlib import Path


def main_function(marker, video, real_size, color, figure, name, angle, resize=None, ref_image=None, ref_dist=None,
                  focal_length=None):
    this_entity = entity.Entity(name=name, figure=figure, color=color, reference_path=marker, real_size=real_size)
    image_location.video_path = video
    location.angle = angle

    if focal_length is not None:
        location.focal_length = focal_length

    if ref_image is not None and ref_dist is not None:
        location.focal_length_finder(marker, ref_image, ref_dist, real_size)

    if resize is not None:
        image_location.resize_video[0] = resize[0]
        image_location.resize_video[1] = resize[1]
    else:
        image_location.resize_video = image_location.frame_size

    this_entity.calc_entity_locations()

    this_entity.to_json()

    while True:
        video_shower.show_with_rect(this_entity.locations, this_entity.image_locations, 5)


if __name__ == '__main__':
    videos_path = Path(__file__).parent.absolute().parent / "videos"
    # marker = str(videos_path / "ball.jpg")
    # video = str(videos_path / "video_2023-06-14_18-40-21.mp4")

    marker = "ball.png"
    video = "video_2023-06-14_18-40-21.mp4"

    ref_img = "photo_2023-06-07_18-13-48.jpg"
    print(marker)
    print(video)

    main_function(marker, video, 0.06, enums.Color.RED, enums.Figure.CUBE, "hello", 110, resize=[480, 640])

    #  location.focal_length_finder(marker, ref_img, 0.2, 0.035)
