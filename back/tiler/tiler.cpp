#include <vips/vips8>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

bool build(std::string dir, std::string name, std::string filename, std::string directory){
    size_t lastIndex = filename.find_last_of('.');
    size_t firstIndex = filename.find_last_of('/') + 1;
    std::string rawName = filename.substr(0, lastIndex);
    rawName = filename.substr(firstIndex, rawName.size());
    std::string savePath = directory + dir + "/";
    fs::create_directories(savePath);
    std::string dzFile = savePath + name;
    std::string thumbnail = savePath + name + ".jpg";
    try{
        vips::VImage image = vips::VImage::new_from_file(filename.c_str());
        image.dzsave(dzFile.c_str());
        int maxLength = std::max(image.width(), image.height());
        image.resize(180.0/maxLength).jpegsave(thumbnail.c_str());
        return true;
    }catch(vips::VError e){
        std::cerr << e.what();
    }
    return false;
}

int main(int argc, char **argv) {
    if (VIPS_INIT(argv[0])) vips_error_exit(nullptr);
    return (build(argv[1], argv[2], argv[3], argv[4]) ? 0 : 1);
}
