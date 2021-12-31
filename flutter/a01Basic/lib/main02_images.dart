import 'package:flutter/material.dart';
import 'package:transparent_image/transparent_image.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:extended_image/extended_image.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Demo',
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            Image.asset(
              'assets/images/sample.gif',
              width: 150,
            ),
            Image.network(
              'https://i.pinimg.com/originals/e9/73/0a/e9730ab2e35d7ec8ac7e432099b5e6d9.gif',
              width: 150,
            ),
            FadeInImage.memoryNetwork(
              placeholder: kTransparentImage,
              image:
                  'https://i.pinimg.com/originals/e9/73/0a/e9730ab2e35d7ec8ac7e432099b5e6d9.gif',
              width: 150,
            ),
            CachedNetworkImage(
              imageUrl:
                  "https://i.pinimg.com/originals/e9/73/0a/e9730ab2e35d7ec8ac7e432099b5e6d9.gif",
              placeholder: (context, url) => CircularProgressIndicator(),
              errorWidget: (context, url, error) => Icon(Icons.error),
              width: 150,
            ),
            ExtendedImage.network(
              "https://i.pinimg.com/originals/e9/73/0a/e9730ab2e35d7ec8ac7e432099b5e6d9.gif",
              width: 150,
              cache: true,
            )
          ],
        ),
      ),
    );
  }
}
