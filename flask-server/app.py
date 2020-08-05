# import time
from flask import Flask
import csv
# import os 
# os.system('sudo pip install sklearn')
print("helo")
import sklearn
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

@app.route('/diningdata')
def diningdata():
    dData = get_diningdata()
    return dData



def get_diningdata():

    with open('hw2_data\door_data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        # tree_clf = DecisionTreeClassifier()
        # model = tree_clf.fit()
        bran_total_swipes = 0
        bran_arr = []
        bran_segments = []
        bran_totals = []
        sill_total_swipes = 0
        sill_arr = []
        sill_segments = []
        sill_totals = []

        bran_1145 = 0
        bran_12 = 0
        bran_1215 = 0

        sill_1145 = 0
        sill_12 = 0
        sill_1215 = 0

        day_count = 0
        day = 0
        day_of_week = 0
        
        for row in csv_reader:

            day = int(row["day"])
            day_of_week = int(row["day_of_week"])
            if day != day_count:

                day_int = day - 1
                if (day_of_week != 0):
                    day_of_week = day_of_week - 1
                else:
                    day_of_week = 6

                # bran_day_arr = []
                # bran_day_arr.insert(0, bran_total_swipes)
                # bran_day_arr.insert(1, day_int)
                # bran_totals.append(bran_day_arr)

                # sill_day_arr = []
                # sill_day_arr.insert(0, sill_total_swipes)
                # sill_day_arr.insert(1, day_int)
                # sill_totals.append(sill_day_arr)

                # bran_day_ = {}
                # bran_day_arr['x'] = bran_total_swipes
                # bran_day_arr['y'] = day_int
                # bran_totals.append(bran_day_arr)

                bran_day_summ = {
                    "x": day_int,
                    "y": bran_total_swipes
                }

                sill_day_summ = {
                    "x": day_int,
                    "y": sill_total_swipes
                }
                # sill_day_arr['x'] = sill_total_swipes
                # sill_day_arr['y'] = day_int
                sill_totals.append(sill_day_summ)
                bran_totals.append(bran_day_summ)

                if bran_1145 > 0:
                    bran_segments.insert(0, bran_1145)
                    bran_segments.insert(1, bran_12)
                    bran_segments.insert(2, bran_1215)
                    bran_segments.insert(3, day_of_week)
                    bran_arr.append(bran_segments)
                    bran_1145 = 0
                    bran_12 = 0
                    bran_1215 = 0
                if sill_1145 > 0:
                    sill_segments.insert(0, sill_1145)
                    sill_segments.insert(1, sill_12)
                    sill_segments.insert(2, sill_1215)
                    sill_segments.insert(3, day_of_week)
                    sill_arr.append(sill_segments)
                    sill_1145 = 0
                    sill_12 = 0
                    sill_1215 = 0
                bran_segments = []
                sill_segments = []
                bran_total_swipes = 0
                sill_total_swipes = 0
                day_count = day_count + 1

            building = row["building"]

            # Check if building is Branford
            if building == "10" and int(row['is_dining_hall']):
                time = int(row["time_of_day"])
                if time >= 690 and time <= 810:
                    bran_total_swipes = bran_total_swipes + 1
                    if time <= 705:
                        bran_1145 = bran_1145 + 1
                        bran_12 = bran_12 + 1
                        bran_1215 = bran_1215 + 1
                    elif time <= 720:
                        bran_12 = bran_12 + 1
                        bran_1215 = bran_1215 + 1
                    elif time <= 735:
                        bran_1215 = bran_1215 + 1

            # Check if building is Silliman
            elif building == "62"and int(row['is_dining_hall']):
                time = int(row["time_of_day"])
                if time >= 690 and time <= 810:
                    sill_total_swipes = sill_total_swipes + 1
                    if time <= 705:
                        sill_1145 = sill_1145 + 1
                        sill_12 = sill_12 + 1
                        sill_1215 = sill_1215 + 1
                    elif time <= 720:
                        sill_12 = sill_12 + 1
                        sill_1215 = sill_1215 + 1
                    elif time <= 735:
                        sill_1215 = sill_1215 + 1


        bran_day_summ = {
            "x": day,
            "y": bran_total_swipes
        }
        bran_totals.append(bran_day_summ)

        sill_day_summ = {
            "x": day,
            "y": sill_total_swipes
        }
        sill_totals.append(sill_day_summ)

        if bran_1145 > 0:
            bran_segments.insert(0, bran_1145)
            bran_segments.insert(1, bran_12)
            bran_segments.insert(2, bran_1215)
            bran_segments.insert(3, day_of_week)
            bran_arr.append(bran_segments)
            bran_1145 = 0
            bran_12 = 0
            bran_1215 = 0
        if sill_1145 > 0:
            sill_segments.insert(0, sill_1145)
            sill_segments.insert(1, sill_12)
            sill_segments.insert(2, sill_1215)
            sill_segments.insert(3, day_of_week)
            sill_arr.append(sill_segments)
            sill_1145 = 0
            sill_12 = 0
            sill_1215 = 0
        bran_segments = []
        sill_segments = []
        bran_total_swipes = 0
        sill_total_swipes = 0
        day_count = day_count + 1

        bran_average = 0
        sill_average = 0

        for i in range(day_count):

            bran_average += bran_totals[i]['y']
            sill_average += sill_totals[i]['y']

        bran_average = bran_average / 28
        sill_average = sill_average / 28

        bran_tree = tree.DecisionTreeClassifier()
        bran_model = bran_tree.fit(bran_arr, bran_score)

        sill_tree = tree.DecisionTreeClassifier()
        sill_model = sill_tree.fit(sill_arr, sill_score)

        bran_tree.predict([[96, 170, 241, 2]])

        dData = {
            "data": [
            {
                "id": "Silliman",
                "color": "hsl(92, 70%, 50%)",
                "data": sill_totals
            },
            {
                "id": "Branford",
                "color": "hsl(232, 70%, 50%)",
                "data": bran_totals
            },
            ]
        }

        return dData

    









    # print("Branford daily average: ", bran_average)
    # print("Silliman daily average: ", sill_average)




    # bran_score = []
    # sill_score = []

    # for i in range(day_count):

    #     if bran_totals[i][0] > bran_average * 1.05:
    #         bran_score.append("above")
    #     elif bran_totals[i][0] < bran_average * 0.95:
    #         bran_score.append("below")
    #     else:
    #         bran_score.append("average")

    #     if sill_totals[i][0] > sill_average * 1.05:
    #         sill_score.append("above")
    #     elif sill_totals[i][0] < sill_average * 0.95:
    #         sill_score.append("below")
    #     else:
    #         sill_score.append("average")



    
    # for i in range(day_count):
    #     print("Branford score for day", i, ":", bran_score[i])
    #     print("Silliman score for day", i, ":", sill_score[i])

# bran_tree = tree.DecisionTreeClassifier()
# bran_model = bran_tree.fit(bran_arr, bran_score)

# sill_tree = tree.DecisionTreeClassifier()
# sill_model = sill_tree.fit(sill_arr, sill_score)

# dot_data = tree.export_graphviz(bran_tree, out_file=None) 
# graph = graphviz.Source(dot_data) 
# graph.render("door_data") 