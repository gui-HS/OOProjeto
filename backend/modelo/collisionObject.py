import pygame

#Class of relationship between two objects at collision
class CollisionObject:

    #Destroy Obj at colision with group2
    def destroy2Obj(self, obj, groupObj2):
        #Iterate through every obj of the group1
        #check to see if obj colided with any obj from group2
        objColided = pygame.sprite.spritecollide(obj, groupObj2, False)
        if objColided:
            groupObj2.remove(objColided)
            return True
        
    #When object from group1 collide with object from group2, destroy obj from group2
    def destroy2Group(self, groupObj1, groupObj2):
        #Iterate through every obj of the group1
        for obj in groupObj1:
            #check to see if obj from group1 colided with any obj from group2
            objColided = pygame.sprite.spritecollide(obj, groupObj2, False)
            if objColided:
                groupObj2.remove(objColided)
                return True

        
    #When objects from group1 and group2 collid, destroy both objects
    def destroyBothObj(self, groupObj1, groupObj2):
        #Iterate through every obj of the first group
        for obj in groupObj1:
            #check to see if obj from group1 colided with any obj from group2
            objColided = pygame.sprite.spritecollide(obj, groupObj2, False)
            if objColided:
                groupObj1.remove(obj)
                groupObj2.remove(objColided)
                return True
