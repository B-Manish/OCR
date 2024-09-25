import OcrToTableTool as ottt
import TableExtractor as te
import TableLinesRemover as tlr
import Functions as fc
import cv2

# table_extractor = te.TableExtractor(path_to_image)
# perspective_corrected_image = table_extractor.execute()
# cv2.imshow("perspective_corrected_image", perspective_corrected_image)


# lines_remover = tlr.TableLinesRemover(perspective_corrected_image)
# image_without_lines = lines_remover.execute()
# cv2.imshow("image_without_lines", image_without_lines)

# ocr_tool = ottt.OcrToTableTool(image_without_lines, perspective_corrected_image)
# ocr_tool.execute()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

path_to_image = "pbd.png"
image = cv2.imread(path_to_image)

greyscaleimg=fc.convert_image_to_grayscale(image)
thresholdimg=fc.threshold_image(greyscaleimg)
invertedimg=fc.invert_image(thresholdimg)
dilatedimg=fc.dilate_image(invertedimg)

# contours=fc.find_contours(dilatedimg,image)
# fc.filter_contours_and_leave_only_rectangles(contours,image)
# fc.find_largest_contour(dilatedimg,image)
# fc.find_largest_contour_with_rectangle(dilatedimg,image)


erode_vertical_lines=fc.erode_vertical_lines(invertedimg)
erode_horizontal_lines=fc.erode_horizontal_lines(invertedimg)
combined_img=fc.combine_eroded_images(erode_vertical_lines,erode_horizontal_lines)
combined_img_dilated=fc.dilate_combined_image_to_make_lines_thicker(combined_img)
image_without_lines=fc.subtract_combined_and_dilated_image_from_original_image(invertedimg,combined_img_dilated)
fc.remove_noise_with_erode_and_dilate(image_without_lines)

# dilated_image=fc.dilate_imagec(thresholdimg)
# fc.find_contoursc(dilated_image,image)

# cv2.imshow("window_name",dilatedimg )
# cv2.waitKey(0)
