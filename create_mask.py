from PIL import Image, ImageDraw

def create_image(width, height):
    # 创建一张空白的白色图片
    image = Image.new("RGB", (width, height), (255, 255, 255))
    return image

def draw_black_rectangles(image, black_rectangles):
    draw = ImageDraw.Draw(image)

    for rect in black_rectangles:
        # rect是一个矩形，以左上角和右下角的坐标表示
        draw.rectangle(rect, fill=(0, 0, 0))

    del draw  # 释放画笔

def save_image(image, filename):
    image.save(filename)

def merge_images(bw_image, rgb_image, output_path):
    # 打开黑白图
    # bw_image = Image.open(bw_image_path).convert("L")  # 转换为灰度图

    # 打开RGB图
    # rgb_image = Image.open(rgb_image_path)

    # 确保两张图像具有相同的大小
    if bw_image.size != rgb_image.size:
        raise ValueError("Image sizes do not match.")

    # 将黑白图转换为RGBA模式，A通道用于透明度
    bw_image_rgba = bw_image.convert("RGBA")

    # 将黑色区域设为透明
    bw_data = bw_image_rgba.getdata()
    new_data = [(100, 0, 0, 100) if pixel[0] == 0 else (0, 100, 0, 100) for pixel in bw_data]
    bw_image_rgba.putdata(new_data)

    # 合并两张图像
    merged_image = Image.alpha_composite(rgb_image.convert("RGBA"), bw_image_rgba)

    # 保存合并后的图像
    merged_image.save(output_path, "PNG")   

if __name__ == "__main__":
    width, height = 1920, 1080

    # 创建一张白色图片
    mask = create_image(width, height)

    # 定义几个矩形区域，以左上角和右下角的坐标表示
    black_rectangles = [
        [0, 0, 260, 50],
        [1550, 0, 1920,50],
        [0, 1000, 550, 1080],
        [550,800,1720,1080]
        # 添加更多的矩形区域...
    ]

    # 在图片上绘制黑色矩形
    draw_black_rectangles(mask, black_rectangles)

    img = Image.open('q.jpg')

    merge_images(mask, img, 'merged.png')

    # 保存图片
    save_image(mask, "mask.png")
