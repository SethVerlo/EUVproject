macro "Crop and save all open images and plot profiles" 
{
	dir = getDirectory("Choose the save folder"); 
	ids=newArray(nImages); 
	for (i=0;i<nImages;i++) 
	{ 
		selectImage(i+1); 
		title = getTitle; 
		ids[i]=getImageID;
		makeRectangle(2, 338, 1022, 262);
		run("Crop");
		saveAs("tiff", dir+title);
		makeRectangle(0, 0, 1022, 262);
		run("Plot Profile");
		Plot.showValues(ids[i]); 
		saveAs("txt", dir+title); 
		close();
	}
}
