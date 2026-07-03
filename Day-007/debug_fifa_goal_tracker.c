#include <stdio.h>

#define STADIUMS 3
#define MAX_GOALS 100
#define PLAYERS 50

int goals[STADIUMS][MAX_GOALS];
int goalCount[STADIUMS];
int playerGoals[PLAYERS];

/* Fixed Function 1 */
void addGoalToStadium2(int minute, int playerID)
{
    if (goalCount[2] >= MAX_GOALS)
    {
        printf("Stadium 2 is full\n");
        return;
    }

    goals[2][goalCount[2]] = minute;

    playerGoals[playerID]++;

    goalCount[2]++;
}

/* Fixed Function 2 */
int totalGoals()
{
    int total = 0;

    for (int s = 0; s < STADIUMS; s++)
    {
        total += goalCount[s];
    }

    return total;
}

/* Fixed Function 3 */
int topScorer()
{
    int maxG = playerGoals[0];
    int winner = 0;

    for (int p = 1; p < PLAYERS; p++)
    {
        if (playerGoals[p] > maxG)
        {
            maxG = playerGoals[p];
            winner = p;
        }
    }

    return winner;
}

/* Fixed Function 4 */
void displayStadium(int stadium)
{
    for (int i = 0; i < goalCount[stadium]; i++)
    {
        printf("%d ", goals[stadium][i]);
    }

    printf("\n");
}