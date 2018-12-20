# VisionScore+
This project is my December 2018 Riot API Challenge submission in the Usability/Practicality category.

VisionScore+ is a graphic statistical tool to help players better understand the importance of vision and ward placement within a League of Legends match. This tool will use a mixture of data visualization, regression, and machine learning to present summoners with an in-depth representation of their ward placement and vision through out any single match or group of matches. Additionally, VisionScore+ will present easy, straight-forward tips to each Summoner based off champion and role selection to optimize their in-match Vision Score, evade potential ganks, and secure kills from wandering champions and potentially dangerous chases.

For a successful and ultimately useful tool, I will have a few primary goals/features for this project:
 - a VisionScore+ metric to ultimately support and leverage the Vision Score found in-match, split into the core areas that affect vision and ultimately vision dominance within a match. (Inspiration: [This Article by 'Riot GMang'](https://boards.na.leagueoflegends.com/en/c/developer-corner/4Pv0FcII-vision-score-details))
 - Showcase a beautiful Summoners Rift map (the 'Map Tool') as the main graphical interface where champion vision and ward vision heatmaps can be overlayed ontop of.
 - Additionally, host a wide set of overlays for the map including champion pathing and kills/deaths/assists markers; aggregation overlays to show most warded and visited locations or most useful- or not- wards; and filters to only show data for other champions, for only champion vision and not ward vision, or by ward type. Anything that can be asked or analyzed regarding match vision, I want to be able to visualize that.
 - For single-match analyses, allow the Map Tool to scrub through the match or play the entire match to view frame-by-frame changes in vision and ward placement across both teams.
 - For multi-match analyses, have a collection of useful aggregate functions and overlays to show progression toward improved (or worsened) Vision Score.
 - And of course, an in-depth and educational wiki so that Summoners can understand how these
 
After these initial, primary goals are met, there are a few secondary goals/features that I would like to achieve/implement:
 - Hose a suite of easy to use but powerful annotation tools to push the boundaries of match-by-match analytics and studying.
 - For single-match analyses, allow the Map Tool to overlay match playbacks for even more performative analytic visualizations.
 - Features to view vision analytics for other champions to compare yours too. This would be useful in comparing teammates or even to higher/lower performing players across servers (think bronze v. challenger ranked players).
 - Allow the tool to be used in conjunction with tournaments to view tiered vision performance through the progression of the tournament or for post-match analytics between competing teams. 
 
Riot API's being used: Standard API's (no Tournament API's)
  - Champion-Mastery-V4
  - League-V4
  - Match-V4
  - Spectator-V4
  - Summoner-V4
 
I am very excited for this project, and I hope you all are as well. Keep in touch here for updates and progress notes!
