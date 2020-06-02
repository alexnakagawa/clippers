<script>
    formidable = require('formidable');
    const bucketName = 'lac_dev_test'
    function handleSubmit() {
        var fileUploadElem = document.getElementById('fileupload');
        console.log(fileUploadElem.value)
    }
</script>

<h1>Hello World!</h1>

<form id='jsonupload' enctype='multipart/form-data' method='post' on:submit|preventDefault={handleSubmit}>
    <input type='file' name='fileupload' id='fileupload' accept='.json'>
    <label for='fileupload'>
        By clicking submit, you will be creating/replacing the json file inside of the `lac_dev_test` bucket in the Google Cloud Project
    </label>
</form>
