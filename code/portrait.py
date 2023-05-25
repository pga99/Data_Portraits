from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


class Portrait:
    def __init__(self, image_path):
        self.fig, self.ax = self.portrait_background()
        self.image_path = image_path
    
    def portrait_background(self):
        fig = plt.figure(figsize=(2, 1.5), dpi=300)
        ax = fig.add_subplot(111)
        plt.xlim([-330, 330])
        plt.ylim([-400, 400])
        
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
        return fig, ax
    
    def add_python_area(self, area_):
        if area_ != ' ':
            img = f"{self.image_path}/Snakes/{area_.replace(' ', '_')}.png"
        else:
            img = f"{self.image_path}/Snakes/AreaNone.png"
        arr_img = plt.imread(img)
        imagebox = OffsetImage(arr_img, zoom=0.15)
        ab = AnnotationBbox(imagebox, (30, 245), frameon=False)
        self.ax.add_artist(ab)

    def add_favourite_object(self, object_):
        if object_ != ' ':
            img = f"{self.image_path}/Objects/{object_.replace(' ', '_')}.png"
            arr_img = plt.imread(img)
            imagebox = OffsetImage(arr_img, zoom=0.15)
            ab = AnnotationBbox(imagebox, (-90, 245), frameon=False)
            self.ax.add_artist(ab)

    def add_working_preference(self, preference_):
        if preference_ != ' ':
            img = f"{self.image_path}/Snakes/{preference_.replace(' ', '_')}.png"   
        else:
            img = f"{self.image_path}/Snakes/RemoteNone.png"
        arr_img = plt.imread(img)
        imagebox = OffsetImage(arr_img, zoom=0.15)
        ab = AnnotationBbox(imagebox, (-190, -240), frameon=False)
        self.ax.add_artist(ab)

    def add_travel_distance(self, distance_):
        if distance_ != ' ':
            img = f"{self.image_path}/Distance/{distance_.replace(' ', '')}.png"  
        else:
            img = f"{self.image_path}/Distance/DistanceNone.png" 
        arr_img = plt.imread(img)
        imagebox = OffsetImage(arr_img, zoom=0.14)
        ab = AnnotationBbox(imagebox, (0, 0), frameon=False)
        self.ax.add_artist(ab)

    def add_water_preference(self, preference_):
        if preference_ != ' ':
            img = f"{self.image_path}/Water/{preference_.replace(' ', '_')}.png" 
            arr_img = plt.imread(img)
            imagebox = OffsetImage(arr_img, zoom=0.135)
            if preference_ == 'Black, hot and with beans':
                ab = AnnotationBbox(imagebox, (-230, -230), frameon=False)
            else: 
                ab = AnnotationBbox(imagebox, (-185, -310), frameon=False)
            self.ax.add_artist(ab)
        else:
            img = f"{self.image_path}/Water/WaterNone.png" 
            arr_img = plt.imread(img)
            imagebox = OffsetImage(arr_img, zoom=0.135)
            ab = AnnotationBbox(imagebox, (-230, -230), frameon=False)
            self.ax.add_artist(ab)

    def add_games(self, preference_):
        if preference_ != ' ':
            img = f"{self.image_path}/Games/{preference_.replace(' ', '_')}.png" 
            arr_img = plt.imread(img)
            imagebox = OffsetImage(arr_img, zoom=0.25)
            ab = AnnotationBbox(imagebox, (50, 15), frameon=False)
            self.ax.add_artist(ab)

    def add_superpower(self, power_):
        if power_ != ' ':
            img = f"{self.image_path}/Superpower/{power_.replace(' ', '_')}.png" 
        else:
            img = f"{self.image_path}/Superpower/PowerNone.png"
        arr_img = plt.imread(img)
        imagebox = OffsetImage(arr_img, zoom=0.13)
        ab = AnnotationBbox(imagebox, (220, -240), frameon=False)
        self.ax.add_artist(ab)

    def add_pyladies(self, pyladies_):
        if pyladies_ == 'yes':
            img = f"{self.image_path}/Snakes/PyLadies.png"
            arr_img = plt.imread(img)
            imagebox = OffsetImage(arr_img, zoom=0.13)
            ab = AnnotationBbox(imagebox, (200, 100), frameon=False)
            self.ax.add_artist(ab)

    def save_portrait(self, path_):
        plt.savefig(path_, bbox_inches=0, pad_inches=0, format='pdf', dpi=300)


categories = {
    'areas': [' ', 'Data', 'Software Development', 'DevOps', 'Web Development','Community', 'Security'],
    'objects': [' ', 'Dictionary', 'List', 'Object', 'MagicMock', 'String'],
    'waters': [' ', 'Still', 'Black, hot and with beans', 'Sparkling', 'With leaves'],
    'workings': [' ', 'On-site', 'Remotely'],
    'distances': [' ', '<10km', '<100km', '<250km', '<500km','<1000km', '1000+ km'],
    'games': [' ', 'Board Games', 'Ball Sport Games', 'Video Games','Mobile phone Games'],
    'powers': [' ', 'Be able to fly', 'Read minds', 'Be invisible whenever you want','Talk to animals', 'Superhuman strength'],
    'pyladies': [' ', 'yes', 'no']
}