
def create_average_image(digit_folder, output_file):
    sum_pixels = [0] * (28 * 28)
    count = 0
    
    for file in os.listdir(digit_folder):
        pixels = read_as_1D(digit_folder + '/' + file)
        
        for i in range(len(pixels)):
            sum_pixels[i] += pixels[i]
        
        count += 1
    
    avg_pixels = []
    for i in range(len(sum_pixels)):
        avg_pixels.append(int(sum_pixels[i] / count))
    
    image = Image.new('L', (28, 28))
    image.putdata(avg_pixels)
    image.save(output_file)

for digit in '0123456789':
    print('Creating average image for digit', digit)
    create_average_image('digits/training/' + digit, 
                         f'average_{digit}.png')
