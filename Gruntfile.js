module.exports = function(grunt) {

    grunt.initConfig({
        copy: {
            main: {
                files: [
                    {
                        src: 'bower_components/flat-ui/dist/css/flat-ui.min.css',
                        dest: 'static/css/flat-ui.min.css'
                    },
                    {
                        src: 'bower_components/flat-ui/dist/css/vendor/bootstrap.min.css',
                        dest: 'static/css/vendor/bootstrap.min.css'
                    },
                    {
                        expand: true,
                        cwd: 'bower_components/flat-ui/fonts/',
                        src: ['**'],
                        dest: 'static/fonts/'
                    }
                ]
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-copy');

    grunt.registerTask('default', ['copy']);
};
