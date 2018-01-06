myApp.factory('BackgroundPic', ($resource) => PicFactoryFunc($resource))

function PicFactoryFunc($resource)
{
    return $resource('/api/RandPhoto/');
}
