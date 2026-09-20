import os
import sys
from assets import pretty_num, better_open

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))

def wheel_output(wheel_scores):
    output_str = "# Global Wheel Points Rankings\n\n|Ranking|Name|Wheel Points|\n| ----------- | ----------- | ----------- |\n"
    
    wheel_scores = dict(sorted(wheel_scores.items(), key=lambda item: -1 * item[1]))

    for index, name in enumerate(wheel_scores):
        output_str += f"|{index + 1}.|{list(wheel_scores)[index]}|{pretty_num(wheel_scores[name])}|\n"

    output_str += "\n## 10 Wheel Points can be exchanged for 1 Owen Point\n"
    output_str += "\n## [Back](../) to Owen Points Leaderboard"

    with better_open('./wheel/README.md', 'w') as wheel_page:
        wheel_page.write(output_str)
    
def wheel_save(wheel_scores):
    with better_open('./wheel/wheel_scores.txt', 'w') as wheel_scores_file:
        wheel_scores_file.write(str(wheel_scores))
