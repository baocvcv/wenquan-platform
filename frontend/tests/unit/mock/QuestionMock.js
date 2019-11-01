import nock from "nock";
import QuestionFactory from "../utils/QuestionFactory.js";

const question_factory = new QuestionFactory();

nock(/.*?/)
  .get("/api/questions/500/")
  .reply(500, {
    result: "Failed"
  });

nock(/.*?/)
  .get("/api/questions/200/")
  .reply(200, question_factory.create_single_choice(200));