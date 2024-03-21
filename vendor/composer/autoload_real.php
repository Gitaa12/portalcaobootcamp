<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit63dd1efbc6a572adb733f8957ae26f08
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    /**
     * @return \Composer\Autoload\ClassLoader
     */
    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        spl_autoload_register(array('ComposerAutoloaderInit63dd1efbc6a572adb733f8957ae26f08', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader(\dirname(__DIR__));
        spl_autoload_unregister(array('ComposerAutoloaderInit63dd1efbc6a572adb733f8957ae26f08', 'loadClassLoader'));

        require __DIR__ . '/autoload_static.php';
        \Composer\Autoload\ComposerStaticInit63dd1efbc6a572adb733f8957ae26f08::getInitializer($loader)();

        $loader->register(true);

        return $loader;
    }
}
