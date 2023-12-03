from PIL import Image, ImageDraw

def create_image(width, height):
    # 创建一张空白的白色图片
    image = Image.new("RGB", (width, height), (255, 255, 255))
    return image

def draw_black_shapes(image, black_shapes):
    draw = ImageDraw.Draw(image)

    for shape in black_shapes:
        if shape['type'] == 'rectangle':
            draw.rectangle(shape['coordinates'], fill=(0, 0, 0))
        elif shape['type'] == 'triangle':
            draw.polygon(shape['coordinates'], fill=(0, 0, 0))

    del draw

def save_image(image, filename):
    image.save(filename)

def merge_images(bw_image, rgb_image, output_path):
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

    #初始mask，全白
    mask = create_image(width, height)

    # 定义绘制字典
    black_shapes = [
        {'type': 'rectangle', 'coordinates': [0, 0, 260, 50]},
        {'type': 'rectangle', 'coordinates': [1550, 0, 1920, 50]},
        {'type': 'rectangle', 'coordinates': [0, 1000, 550, 1080]},
        # {'type': 'rectangle', 'coordinates': [550, 800, 1720, 1080]},
        {'type': 'triangle', 'coordinates': [(1111, 810), (610, 1080), (1793, 1080)]},
        # Add more shapes...
    ]
    # 绘制
    draw_black_shapes(mask, black_shapes)

    img = Image.open('q.jpg')

    merge_images(mask, img, 'merged.png')

    save_image(mask, "mask.jpg")
