from pyecharts.charts import Pie

if __name__ =="__main__":

    position = ['area i', 'area ii', 'area iii', 'area iv']

    num = [20, 10, 30, 40]

    pie = pie("销售分布", title_pos='center', width=900, title_text_size=20)

    pie.add("区域", position, num,

            center=[50, 50],

            is_random=false,

            radius=[30, 75],

            rosetype='area',

            is_legend_show=false,

            is_label_show=true, label_text_size=20)

    pie.render()