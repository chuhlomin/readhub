module.exports = function(grunt) {

    grunt.initConfig({
        cssmin: {
            combine: {
                files: {
                    'readhub/static/css/main.min.css': ['readhub/static/css/main.css']
                }
            }
        },
        concat: {
            basic: {
                src: [
                    'bower_components/flat-ui/dist/css/vendor/bootstrap.min.css',
                    'bower_components/flat-ui/dist/css/flat-ui.min.css',
                    'readhub/static/css/main.min.css'
                ],
                dest: 'readhub/static/css/application.css'
            }
        },
        copy: {
            main: {
                files: [
                    {
                        expand: true,
                        cwd: 'bower_components/flat-ui/fonts/',
                        src: ['**'],
                        dest: 'readhub/static/fonts/'
                    }
                ]
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-copy');

    grunt.registerTask('default', ['cssmin', 'concat', 'copy']);
};
