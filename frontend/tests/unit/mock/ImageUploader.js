import nock from "nock";

nock(/.*?/)
  .post("/api/upload/image/")
  .reply(200, {
    data: { url: "/media/pictures/image1.jpg" }
  });
