#Main Program
import FileReader
import GraphMaker
import PointsExtractor

def main():

    print("Main Program")
    
    FileReader.readfile()
    (x,y) = PointsExtractor.extracting_points()
    GraphMaker.plotgraph(x,y)

    gaps =[]
    for i in range(0, len(x)):
        gaps.append( abs(y[i] - x[i])) #Obtains the gap between each point

    gap_strategicDirection = ["Strategic vision", "Strategic planning", "Consumer experience", "Competitive strategy","Operating environment strategy" , "Strategic execution" , "Core capabilities"]
    gap_structure_and_process = ["Organizational design", "Job and work group design", "Operational alignment and integration", "Strategic alliances/ partnerships", "Developing new ventures", "Organizational governance", "Organizational communication"]

    GraphMaker.radarplot(gap_strategicDirection, gaps[0:7] )


if __name__ == "__main__" :
    main()