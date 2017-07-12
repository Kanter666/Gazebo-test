#include <gazebo/gazebo.hh>
#include <sstream>

#include <gazebo/msgs/msgs.hh>
#include <gazebo/common/Console.hh>
#include <gazebo/gui/GuiEvents.hh>
#include <gazebo/math/Quaternion.hh>
#include <gazebo/common/MouseEvent.hh>
#include <gazebo/rendering/UserCamera.hh>
#include <gazebo/transport/Publisher.hh>
#include <gazebo/gui/BoxMaker.hh>

namespace gazebo
{
  class WorldPluginTutorial : public WorldPlugin, public BoxMaker
  {
    public: WorldPluginTutorial() : WorldPlugin()
            {
              printf("Hello World!\n");
              this->CreateTheEntity();
            }

    public: void Load(physics::WorldPtr _world, sdf::ElementPtr _sdf)
            {
            }
  };
  GZ_REGISTER_WORLD_PLUGIN(WorldPluginTutorial)
}

std::string gazebo::WorldPluginTutorial::GetSDFString()
{
  std::ostringstream newModelStr;
  newModelStr << "<sdf version ='" << SDF_VERSION << "'>"
    << "<model name='unit_box_" << counter << "'>"
    << "<pose>0 0 0.5 0 0 0</pose>"
    << "<link name ='link'>"
    <<   "<inertial><mass>1.0</mass></inertial>"
    <<   "<collision name ='collision'>"
    <<     "<geometry>"
    <<       "<box>"
    <<         "<size>1.0 1.0 1.0</size>"
    <<       "</box>"
    <<     "</geometry>"
    << "</collision>"
    << "<visual name ='visual'>"
    <<     "<geometry>"
    <<       "<box>"
    <<         "<size>1.0 1.0 1.0</size>"
    <<       "</box>"
    <<     "</geometry>"
    <<     "<material>"
    <<       "<script>"
    <<         "<uri>file://media/materials/scripts/gazebo.material</uri>"
    <<         "<name>Gazebo/Grey</name>"
    <<       "</script>"
    <<     "</material>"
    <<   "</visual>"
    << "</link>"
    << "</model>"
    << "</sdf>";

  return newModelStr.str();
}

void gazebo::WorldPluginTutorial::CreateTheEntity()
{
  msgs::Factory msg;

  math::Vector3 p = math::Vector3(1, 1, 1);
  math::Vector3 size = math::Vector3((double)rand(), (double)rand(), (double)rand());

  msg.set_sdf(this->GetSDFString());

  this->makerPub->Publish(msg);
}