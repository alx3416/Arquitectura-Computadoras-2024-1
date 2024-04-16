#ifndef CPPBASICS_IMAGE_UTILS_H
#define CPPBASICS_IMAGE_UTILS_H

#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <cmath>
#include <omp.h>

namespace myLib{

    cv::Mat gammaCorrectionPassByValue(cv::Mat frame_gray){
        double value = 0;
        for(int row=0; row<frame_gray.rows; row++){
            for(int col=0; col<frame_gray.cols; col++){
                value = static_cast<double>(frame_gray.at<uint8_t >(row, col));
                value = value / 255;
                value = pow(value, 0.3);
                value = value * 255;
                frame_gray.at<uint8_t >(row, col) = static_cast<uint8_t>(value);
            }
        }
        return frame_gray;
    }

    void gammaCorrectionPassByReference(cv::Mat &frame_gray){
        double value = 0;
        for(int row=0; row<frame_gray.rows; row++){
            for(int col=0; col<frame_gray.cols; col++){
                value = static_cast<double>(frame_gray.at<uint8_t >(row, col));
                value = value / 255;
                value = pow(value, 0.3);
                value = value * 255;
                frame_gray.at<uint8_t >(row, col) = static_cast<uint8_t>(value);
            }
        }

    }
    uint8_t kernelmultiplyPassByReference(cv::Mat& kernel, cv::Mat& patch) {
        double value = 0;
        for (int row = 0; row < patch.rows; row++) {
            for (int col = 0; col < patch.cols; col++) {
                value += (static_cast<double>(patch.at<uint8_t>(row, col))/255) * kernel.at<double>(row, col);
            }
        }
        return static_cast<uint8_t>((value+9.0)*(255.0/18.0));
    }
    
    
    void filterPassByReference(cv::Mat& frame_gray) {
        cv::Mat kernel = (cv::Mat_<double>(3, 3) << 0, -1, 0, 0, -1, 0, 0, -1, 0);
        cv::Mat localPatch;
        for (int row = 1; row < frame_gray.rows-1; row++) {
            for (int col = 1; col < frame_gray.cols-1; col++) {
                localPatch = frame_gray(cv::Range(row-1, row+2),
                                        cv::Range(col-1, col+2));
                // Multiplicamos punto a punto, el resultado es el nuevo pixel
                frame_gray.at<uint8_t >(row, col) = kernelmultiplyPassByReference(kernel, localPatch);
            }
        }
    }


    void filterPassByReferenceParallel(cv::Mat& frame_gray) {
        cv::Mat kernel = (cv::Mat_<double>(3, 3) << 0, -1, 0, 0, -1, 0, 0, -1, 0);
        cv::Mat localPatch;
// #pragma omp parallel for shared(frame_gray)
        for (int row = 1; row < frame_gray.rows-1; row++) {
            for (int col = 1; col < frame_gray.cols-1; col++) {
                localPatch = frame_gray(cv::Range(row-1, row+2),
                                        cv::Range(col-1, col+2));
                // Multiplicamos punto a punto, el resultado es el nuevo pixel
                frame_gray.at<uint8_t >(row, col) = kernelmultiplyPassByReference(kernel, localPatch);
            }
        }
    }
} // namespace myLib

#endif //CPPBASICS_IMAGE_UTILS_H
