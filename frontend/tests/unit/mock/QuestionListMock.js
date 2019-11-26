import nock from "nock";
import QuestionFactory from "../utils/QuestionFactory.js";

const question_factory = new QuestionFactory();

nock(/.*?/)
  .get("/api/question_banks/500/")
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .get("/api/question_banks/501/")
  .reply(200, {
    questions: [500]
  });

nock(/.*?/)
  .get("/api/questions/500/")
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .get("/api/question_banks/1/")
  .reply(200, {
    questions: [1]
  });

nock(/.*?/)
  .get("/api/questions/1/")
  .reply(200, question_factory.create_single_choice(1));

nock(/.*?/)
  .get("/api/questions/2/")
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .get("/api/question_banks/2/")
  .reply(200, {
    questions: []
  });

nock(/.*?/)
  .get("/api/questions/3/")
  .reply(200, question_factory.create_single_choice(3));
