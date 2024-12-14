import matplotlib.pyplot as plt
def data_visualization_dashboard():
    categories = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 25]
    plt.bar(categories, values)
    plt.title('Category Distribution')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()
data_visualization_dashboard()
