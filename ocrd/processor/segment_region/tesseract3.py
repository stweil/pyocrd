from ocrd.model import OcrdPage
from ocrd.processor import Processor
from ocrd.utils import getLogger
import tesserocr
import PIL

log = getLogger('processor.segment_region.tesseract3')

class Tesseract3RegionSegmenter(Processor):

    def process(self):
        """
        Performs the region segmentation.
        """
        with tesserocr.PyTessBaseAPI() as tessapi:
            for input_file in self.workspace.mets.files_in_group(self.inputGrp):
                self.workspace.download_file(input_file)
                page = OcrdPage.from_file(input_file)
                image_filename = self.workspace.download_url(page.imageFileName)
                image = PIL.Image.open(image_filename)
                tessapi.SetImage(image)
                log.debug("Detecting regions with tesseract")
                for component in tessapi.GetComponentImages(tesserocr.RIL.BLOCK, True):
                    box, index = component[1], component[2]
                    # the region reference in the reading order element
                    region_ref = "r%i" % index
                    page.add_reading_order_ref(region_ref, index)
                    page.add_text_region(region_ref, box)
                self.workspace.add_file(self.outputGrp, basename=input_file.basename_without_extension + '.xml', content=page.to_xml())