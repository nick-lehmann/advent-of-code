module.exports = {
  prompt: ({ prompter, args }) => {
    const questions = [
      {
        type: "input",
        name: "year",
        message: "What's the year?",
      },
      {
        type: "input",
        name: "day",
        message: "What's the day?",
      },
      {
        type: "input",
        name: "name",
        message: "What's the name of the day?",
      },
    ];

    return prompter.prompt(questions).then((answers) => {
      answers["dayPadded"] = answers["day"].padStart(2, "0");
      return answers;
    });
  },
};
