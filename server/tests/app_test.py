from project.app import app


def test_ping():
    tester = app.test_client()
    response = tester.get("/ping", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b'"pong!"\n'


# def test_books(): 
#     tester = app.test_client()
#     response = tester.get("/books", content_type="html/text")

#     assert response.status_code == 200
#     assert response.data == "test"