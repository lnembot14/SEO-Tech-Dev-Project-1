CREATE DATABASE IF NOT EXISTS worldcup;
DROP TABLE IF EXISTS favoriteTeams;

CREATE TABLE favoriteTeams (
    id INT(8) UNSIGNED NOT NULL auto_increment,
    team_name VARCHAR(100) default NULL,
    world_cup_titles INT(3) UNSIGNED default NULL,
    matches_played INT(8) UNSIGNED default NULL,
    world_cup_wins INT(8) UNSIGNED default NULL,
    world_cup_losses INT(8) UNSIGNED default NULL,
    world_cup_draws INT(8) UNSIGNED default NULL,
    goals_for INT(8) UNSIGNED default NULL,
    goals_against INT(8) UNSIGNED default NULL,
    PRIMARY KEY (id)
) AUTO_INCREMENT=1;