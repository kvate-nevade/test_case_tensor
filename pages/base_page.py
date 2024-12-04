import os
class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def switch_to_window(self, number):
        window_name = self.browser.window_handles[number - 1]
        self.browser.switch_to.window(window_name)

    def check_same_images_sizes(self, images):
        if not images:
            raise ValueError("No images found to compare")
        first_image = images[0]
        first_image_size = first_image.size
        for image in images:
            current_image_size = image.size
            #print(current_image_size['height'], first_image_size['height'])
            assert current_image_size['height'] == first_image_size['height'], 'Images hight not the same'
            assert current_image_size['width'] == first_image_size['width'], 'Images width not the same'

