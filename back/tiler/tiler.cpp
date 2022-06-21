#include <vips/vips8>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

std::string build(std::string filename, std::string directory){
    size_t lastIndex = filename.find_last_of('.');
    std::string rawName = filename.substr(0, lastIndex);
    std::string savePath = directory + rawName + "/";
    fs::create_directories(savePath);
    std::string dzFile = savePath + rawName + ".dz";
    std::string thumbnail = savePath + rawName + ".jpg";

    try{
        vips::VImage image = vips::VImage::new_from_file(filename.c_str());
        image.dzsave(dzFile.c_str(), vips::VImage::option()->set("depth", VIPS_FOREIGN_DZ_DEPTH_ONETILE));
        int maxLength = std::max(image.width(), image.height());
        image.resize(180.0/maxLength).jpegsave(thumbnail.c_str());
    }catch(vips::VError e){
        std::cerr << e.what();
    }
    return savePath;
}
