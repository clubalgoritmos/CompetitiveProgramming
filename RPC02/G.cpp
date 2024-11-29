#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

double dist(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

string get_shape(vector<Point>& points) {
    vector<double> side_lengths = {dist(points[0], points[1]), dist(points[1], points[2]), dist(points[2], points[3]), dist(points[3], points[0])};
    vector<double> diag_lengths = {dist(points[0], points[2]), dist(points[1], points[3])};

    bool all_sides_equal = side_lengths[0] == side_lengths[1] && side_lengths[1] == side_lengths[2] && side_lengths[2] == side_lengths[3];
    bool all_diags_equal = diag_lengths[0] == diag_lengths[1];
    bool opposite_sides_equal = side_lengths[0] == side_lengths[2] && side_lengths[1] == side_lengths[3];
    bool diags_perpendicular = (points[0].x-points[2].x)*(points[1].x-points[3].x) + (points[0].y-points[2].y)*(points[1].y-points[3].y) == 0;

    if (all_sides_equal && diags_perpendicular) {
        return "square";
    } else if (diags_perpendicular && opposite_sides_equal) {
        return "rectangle";
    } else if (all_sides_equal) {
        return "rhombus";
    } else if (opposite_sides_equal) {
        return "parallelogram";
    } else if (all_diags_equal) {
        return "kite";
    } else if (side_lengths[0] == side_lengths[2] || side_lengths[1] == side_lengths[3]) {
        return "trapezium";
    } else {
        return "none";
    }
}

int main() {
    vector<Point> points(4);
    for (int i = 0; i < 4; ++i) {
        cin >> points[i].x >> points[i].y;
    }
    cout << get_shape(points) << endl;
    return 0;
}