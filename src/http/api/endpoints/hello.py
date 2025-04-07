import falcon

class HelloResource:
    async def on_get(self, req, resp, user_id):
        # Get user from service layer
        resp.media = {"message": f"hello {user_id}"}
        resp.status = falcon.HTTP_200
